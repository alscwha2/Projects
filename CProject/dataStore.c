#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include "dataStore.h"
#define CAR_SIZE sizeof(car)
#define MAX_CARS_IN_MEMORY (max_memory / CAR_SIZE)
#define MRUindex numberOfCarsInMemory - 1
#define LRU carsInMemory[0]

typedef struct Car {
	char* make;
	char* model; 
	short year; 
	long price;
	int uniqueID;
} car;

static car* buffer;

static FILE* carsOnDisk = NULL;
static int numberOfCarsOnDisk = 0;

static car *carsInMemory = NULL;
static int numberOfCarsInMemory = 0;
static int max_memory = 0;

static int initialized = 0;

static int initialize() {
	freopen("output.txt", "w", stderr);
	fprintf(stderr, "%s\n", "redirected stderr to output.txt file");

	carsOnDisk = fopen("carsOnDisk.txt", "w+");
	if (carsOnDisk == NULL) {
		fprintf(stderr, "%s\n", "ERROR CREATING carsOnDisk.txt FILE");
		return EXIT_FAILURE;
	}
	fprintf(stderr, "%s\n", "created carsOnDisk file");

	fprintf(stderr, "buffer: %p, ", buffer);
	buffer = calloc(1, CAR_SIZE);
	fprintf(stderr, "buffer initialized: %p\n", buffer);

	initialized = 1;

	return EXIT_SUCCESS;
}

/**********************************************************************
STATIC METHODS
***********************************************************************/

/*********************
DECLARATIONS
*********************/
static void writeCarToDisk(car c);
static car *getCarFromDisk(int id);
static void deleteCurrentCarFromDisk();
static int deleteCarOnDisk(int id);

static void moveLRUtoDisk();
static int loadCarsFromDisk();
static car getAndDeleteLastCarOnDisk();
static void writeCarToMemory(car c);
static car *getCarFromMemory(int id);
static void setCarMRU(int index);
static int deleteCarInMemory(int id);


/*********************
DISPLAY FUNCTIONS
*********************/
static void displayMemory() {
	if (carsInMemory == NULL) {
		fprintf(stderr, "%s\n", "ERROR: CALLED displayMemory() WITH UNINITIALIZED ARRAY");
		return;
	}

	fprintf(stderr, "Memory:{");
	for (int i = 0; i < numberOfCarsInMemory; i++) {
		fprintf(stderr, "%d, ", carsInMemory[i].uniqueID);
	}
	fprintf(stderr, "}\n");
}

static void displayDisk() {
	if (carsOnDisk == NULL) {
		fprintf(stderr, "%s\n", "ERROR: CALLED displayDisk WITH UNOPENED output.txt FILE");
		return;
	}

	rewind(carsOnDisk);
	fprintf(stderr, "%s", "Disk: {");
	while(1) {
		fread(buffer, CAR_SIZE, 1, carsOnDisk);
		if (feof(carsOnDisk)) break;
		fprintf(stderr, "%d, ", buffer[0].uniqueID);
	}
	fprintf(stderr, "}\n");
}

/*********************
DISK
*********************/

static void writeCarToDisk(car c) {
	fprintf(stderr, "%s%d\n", "writeCarToDisk(): id: ", c.uniqueID);
	buffer[0] = c;
	int errno = fwrite(buffer, CAR_SIZE, 1, carsOnDisk);
	if (errno == 0) printf("ERROR WRITING CAR TO DISK\n");
	numberOfCarsOnDisk++;
}

static car *getCarFromDisk(int id) {
	fprintf(stderr, "fetching car from disk: ID: %d\n", id);
	rewind(carsOnDisk);
	for (int i = 0; i < numberOfCarsOnDisk; i++) {
		fread(buffer, CAR_SIZE, 1, carsOnDisk);
		if (buffer->uniqueID == id) {
			fprintf(stderr, "car found on disk\n");
			if (MAX_CARS_IN_MEMORY > 0) {
				deleteCurrentCarFromDisk();
				car c = buffer[0];
				moveLRUtoDisk();
				writeCarToMemory(c);
				return carsInMemory + MRUindex;
			}
			fseek(carsOnDisk, 0, SEEK_END);
			return buffer;
		}
	}

	return NULL;
}

static void deleteCurrentCarFromDisk() {
	fprintf(stderr, "deleteCurrentCarFromDisk(): deleting car from disk\n");
	//find offset of car to delete
	long car_pos = ftell(carsOnDisk) - CAR_SIZE;
	long fileSize = numberOfCarsOnDisk * CAR_SIZE;

	char *fileBuffer = malloc(fileSize - (car_pos + CAR_SIZE));
	fseek(carsOnDisk, car_pos + CAR_SIZE, SEEK_SET);
	for(int i = 0; 1; i++) {
		char c = fgetc(carsOnDisk);
		if (feof(carsOnDisk)) break;
		fileBuffer[i] = c;
	}
	
	fseek(carsOnDisk, car_pos, SEEK_SET);
	for(int i = 0; i < fileSize - (car_pos + CAR_SIZE); i++) fputc(fileBuffer[i], carsOnDisk);
	ftruncate(fileno(carsOnDisk), fileSize - CAR_SIZE);

	numberOfCarsOnDisk--;
}

static int deleteCarOnDisk(int id) {
	rewind(carsOnDisk);
	for (int i = 0; i < numberOfCarsOnDisk; i++) {
		fread(buffer, CAR_SIZE, 1, carsOnDisk);
		if (buffer->uniqueID == id) {
			deleteCurrentCarFromDisk();
			return EXIT_SUCCESS;
		}
	}
	return EXIT_FAILURE;
}

/*********************
MEMORY
*********************/

/*
 * lRU should always be in position 0
 */
static void moveLRUtoDisk() {
	fseek(carsOnDisk, 0, SEEK_END);
	fprintf(stderr, "%s%d\n", "moveLRUtoDisk(): id: ", LRU.uniqueID);
	writeCarToDisk(LRU);
	for (int i = 0; i < numberOfCarsInMemory-1; i++) carsInMemory[i] = carsInMemory[i+1];
	numberOfCarsInMemory--;
	fprintf(stderr, "New ");
	displayMemory();
	fprintf(stderr, "New ");
	displayDisk();
}

static int loadCarsFromDisk() {
	int numberOfCarsToLoad = MAX_CARS_IN_MEMORY - numberOfCarsInMemory;
	numberOfCarsToLoad = (numberOfCarsToLoad < numberOfCarsOnDisk) ? numberOfCarsToLoad : numberOfCarsOnDisk;
	fprintf(stderr, " loadCarsFromDisk(): number of cars to load: %d\nprevious: ", numberOfCarsToLoad);
	displayMemory();
	displayDisk();

	for (int i = 0; i < numberOfCarsInMemory; i++) {
		carsInMemory[numberOfCarsInMemory + numberOfCarsToLoad - 1 - i] = carsInMemory[numberOfCarsInMemory - 1 - i];
	}
	for (int i = 0; i < numberOfCarsToLoad; i++) {
		carsInMemory[numberOfCarsToLoad - 1 - i] = getAndDeleteLastCarOnDisk();
	}
	numberOfCarsInMemory += numberOfCarsToLoad;

	fprintf(stderr, "new:\n");
	displayMemory();
	displayDisk();
}
//HELPER
static car getAndDeleteLastCarOnDisk() {
	fseek(carsOnDisk, 0 - CAR_SIZE, SEEK_END);
	fread(buffer, CAR_SIZE, 1, carsOnDisk);
	numberOfCarsOnDisk--;
	ftruncate(fileno(carsOnDisk), numberOfCarsOnDisk * CAR_SIZE);
	return buffer[0];
}

static void writeCarToMemory(car c) {
	fprintf(stderr, "%s%d\n", "writeCarToMemory(): id: ", c.uniqueID);
	numberOfCarsInMemory++;
	carsInMemory[MRUindex] = c;
}

static car *getCarFromMemory(int id) {
	fprintf(stderr, "fetching car from memory: ID: %d\n", id);
	car *cptr = carsInMemory;
	for (int i = 0; i < numberOfCarsInMemory; i++) {
		if (cptr[i].uniqueID == id) {
			fprintf(stderr, "car found in memory. setting as MRU\n");
			setCarMRU(i);
			return cptr + MRUindex;
		}
	}

	return NULL;
}
//HELPER FUNCTION
static void setCarMRU(int index) {
	car c = carsInMemory[index];
	for (int i = index + 1; i < numberOfCarsInMemory; i++) carsInMemory[i-1] = carsInMemory[i]; 
	carsInMemory[MRUindex] = c;
}

static int deleteCarInMemory(int id) {
	car *cptr = getCarFromMemory(id);
	if (cptr == NULL) return EXIT_FAILURE;
	numberOfCarsInMemory--;
	loadCarsFromDisk();
	return EXIT_SUCCESS;
}

/**********************************************************************
NON-STATIC METHODS
***********************************************************************/

int addCar(char* make, char* model, short year, long price, int uniqueID) {
	if (!initialized) initialize();

	fprintf(stderr, "%s%d\n", " addCar(): id: ",uniqueID);
	char *makecpy = malloc(strlen(make) + 1);
	strcpy(makecpy, make);
	char *modelcpy = malloc(strlen(model) + 1);
	strcpy(modelcpy, model);

	car c = {makecpy, modelcpy, year, price, uniqueID};
	if (numberOfCarsInMemory < MAX_CARS_IN_MEMORY) {
		writeCarToMemory(c);
		displayMemory();
	} else if (MAX_CARS_IN_MEMORY == 0) {
		writeCarToDisk(c);
		displayDisk();
	} else {
		moveLRUtoDisk();
		writeCarToMemory(c);
		displayMemory();
		displayDisk();
	}
	return EXIT_SUCCESS;
}

struct Car* getCarById(int id) {
	if (!initialized) initialize();

	car *cptr = getCarFromMemory(id);
	if (cptr == NULL) {
		fprintf(stderr, "car ID: %d not found in memory\n", id);
		cptr = getCarFromDisk(id);
	}
	return cptr;
}

int deleteCarById(int id) {
	if (!initialized) initialize();

	if (deleteCarInMemory(id) == EXIT_SUCCESS) {
		fprintf(stderr, "delete car ID: %d from memory\n", id);
		return EXIT_SUCCESS;
	}

	return deleteCarOnDisk(id);
}

int modifyCarById(int id, struct Car* myCar) {
	if (!initialized) initialize();

	if (id != myCar->uniqueID) return EXIT_FAILURE;
	car *cptr = getCarById(id);
	if (cptr == NULL) return EXIT_FAILURE;

	fprintf(stderr, "modifyCarById(%d):\n", id);
	fprintf(stderr, "previous: {%s, %s, %d, %d, %d}\n", cptr->make, cptr->model, cptr->year, cptr->price, cptr->uniqueID);
	cptr->make = malloc(strlen(myCar->make) + 1);
	strcpy(cptr->make, myCar->make);
	cptr->model = malloc(strlen(myCar->model) + 1);
	strcpy(cptr->model, myCar->model);
	cptr->year = myCar->year;
	cptr->price = myCar->price;
	fprintf(stderr, "new: {%s, %s, %d, %d, %d}\n", cptr->make, cptr->model, cptr->year, cptr->price, cptr->uniqueID);

	return EXIT_SUCCESS;

}

/*********************
MEMORY
*********************/

int setMaxMemory(size_t bytes) {
	if (!initialized) initialize();
	fprintf(stderr, " setMaxMemory(%d)\n", bytes);
	if (bytes < 0) {
		fprintf(stderr, "%s\n", "attempt to set max_memory to less than zero");
		return EXIT_FAILURE;
	}

	fprintf(stderr, "previous max_memory: %d previous MAX_CARS_IN_MEMORY: %d, CAR_SIZE: %d\n", max_memory, MAX_CARS_IN_MEMORY, CAR_SIZE);

	//if new value will not change the number of cars allowed in memory do nothing
	if (max_memory / CAR_SIZE == bytes / CAR_SIZE) {
		fprintf(stderr, "setMaxMemory(%d): does not add any more cars to array. Aborting.\n", bytes);
		return EXIT_FAILURE;
	}

	//initialize carsInMemory array
	else if (carsInMemory == NULL) {
		fprintf(stderr, "%s%p", "initilizing carsInMemory array: previous: ", carsInMemory);
		carsInMemory = (car *)calloc(bytes / CAR_SIZE, CAR_SIZE);
		fprintf(stderr, "%s%p\n", " new: ", carsInMemory);
		max_memory = bytes;
		loadCarsFromDisk();
	}
	//if we need to shrink the array then move the required amount of cars to disk
	else if (bytes < max_memory) {
		fprintf(stderr, "%s\n", "shrinking array size");
		int numberOfCarsToLoad = numberOfCarsInMemory - (bytes / CAR_SIZE);
		for (int i = 0; i < numberOfCarsToLoad; i++) moveLRUtoDisk();
		carsInMemory = (car *) realloc(carsInMemory, bytes - (bytes % CAR_SIZE));
	} else {
		//change array size
		fprintf(stderr, "%s\n", "expanding array size");
		carsInMemory = (car *)realloc(carsInMemory, bytes - (bytes % CAR_SIZE));
		max_memory = bytes;
		loadCarsFromDisk();
	}

	max_memory = bytes;
	
	fprintf(stderr, "new max_memory: %d\nnew MAX_CARS_IN_MEMORY: %d\n", max_memory, MAX_CARS_IN_MEMORY);
	return EXIT_SUCCESS;
}

int getNumberOfCarsInMemory() {
	if (!initialized) initialize();
	return numberOfCarsInMemory;
}

int getAmountOfUsedMemory() {
	if (!initialized) initialize();
	return numberOfCarsInMemory * CAR_SIZE;
}

struct Car* getAllCarsInMemory() {
	if (!initialized) initialize();
	return carsInMemory;
}

/*********************
DISK
*********************/

int getNumberOfCarsOnDisk() {
	if (!initialized) initialize();
	return numberOfCarsOnDisk;
}

/* this function does NOT cause the cars on disk to displace those
* that were already in memory. It uses separate memory to load them
* and return them to the caller. THE CALLER MUST FREE THIS MEMORY
* WHEN FINISHED WITH THESE CARS.
*/
struct Car* getAllCarsOnDisk() {
	if (!initialized) initialize();
	car *c = (car *)calloc(numberOfCarsOnDisk, CAR_SIZE);
	fprintf(stderr, "%s%d\n", "getAllCarsOnDisk(): numberOfCarsOnDisk: ", numberOfCarsOnDisk);
	fseek(carsOnDisk, 0, SEEK_SET);
	int errno = fread(c, CAR_SIZE, numberOfCarsOnDisk, carsOnDisk);
	if (errno == 0) fprintf(stderr, "%s\n", "ERROR READING CARS FROM carsOnDisk FILE");
	displayDisk();
	return c;
}