#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "dataStore.c"

static int id = 0;
void testMaxMemoryAndAddCar();
void testCarGetters();
void testIntGetters();
void testGetCarById();
void testDeleteCarById();
void testModifyCarById();

void printAllCarsInMemory();
void printAllCarsOnDisk();
void printMemory();
void addManyCars(int amount);

void testMaxMemoryAndAddCar() {
	printf(" _____________________________________\n");
	printf("|***** testMaxMemoryAndAddCar(): *****|\n");
	printf("|_____________________________________|\n");

	//before setMaxMemory() has been called
	printf("___________________________________________________________\n");
	printf("*** test adding cars before setMaxMemory() has been called:\n");
	printMemory();
	addManyCars(10);
	printMemory();
	testCarGetters();

	//calling setMaxMemory() with cars already written on disk
	printf("_________________________________________________________________\n");
	printf("*** test calling setMaxMemory() with cars already written to disk\n");
	printf("setMaxMemory(%d)\n", 200);
	setMaxMemory(200);
	printMemory();
	testCarGetters();

	printf("_____________________________________\n");
	printf("*** test adding cars with full memory\n");
	//adding cars with new full memory
	addManyCars(10);
	printMemory();
	testCarGetters();

	//shrinking maxMemory
	printf("____________________________\n");
	printf("*** test lowering maxMemory\n");
	printf("setMaxMemory(%d)\n", 80);
	setMaxMemory(80);
	printMemory();
	testCarGetters();

}

void testCarGetters() {
	printAllCarsInMemory();
	printAllCarsOnDisk();
}

void testIntGetters() {
	printMemory();
}

void testGetCarById() {
	printf(" _____________________________\n");
	printf("|***** testGetCarById(): *****|\n");
	printf("|_____________________________|\n");
	printf("____________________________\n");
	printf("*** test getting from memory\n");
	car *c = getCarById(18);
	printf("testGetCarById(18):\n {make = %s, model = %s, year = %d, price = %d, Id = %d}\n", c->make, c->model, c->year, c->price, c->uniqueID);
	testCarGetters();
	printf("__________________________\n");
	printf("*** test getting from disk\n");
	c = getCarById(5);
	printf("testGetCarById(5):\n {make = %s, model = %s, year = %d, price = %d, Id = %d}\n", c->make, c->model, c->year, c->price, c->uniqueID);
	testCarGetters();
}

void testDeleteCarById() {
	printf(" ________________________________\n");
	printf("|***** testDeleteCarById(): *****|\n");
	printf("|________________________________|\n");
	printf("_________________________________\n");
	printf("*** test deleting car from memory\n");
	printf("deleteCarById(18)\n");
	deleteCarById(18);
	testCarGetters();
	printf("_______________________________\n");
	printf("*** test deleting car from disk\n");
	printf("deleteCarById(2)\n");
	deleteCarById(2);
	testCarGetters();
}

void testModifyCarById() {
	printf(" ________________________________\n");
	printf("|***** testModifyCarById(): *****|\n");
	printf("|________________________________|\n");
	printf("_______________________________\n");
	printf("**** test modifying from memory\n");
	printf("modifyCarById(18)\n");
	car *cptr = getCarById(18);
	printf("previous:\n {make = %s, model = %s, year = %d, price = %d, Id = %d}\n", cptr->make, cptr->model, cptr->year, cptr->price, cptr->uniqueID);
	cptr = (car *) malloc(CAR_SIZE);
	car c = {"NewMake", "NewModel", 1, 1, 18};
	*cptr = c;
	modifyCarById(18, cptr);
	cptr = getCarById(18);
	printf("new:\n {make = %s, model = %s, year = %d, price = %d, Id = %d}\n", cptr->make, cptr->model, cptr->year, cptr->price, cptr->uniqueID);
	testCarGetters();
	printf("____________________________\n");
	printf("*** test modifying from disk\n");
	printf("modifyCarById(6):\n");
	cptr = malloc(CAR_SIZE);
	c.uniqueID = 6;
	*cptr = c;
	modifyCarById(6, cptr);
	testCarGetters();
}

void printAllCarsInMemory() {
	car *c = getAllCarsInMemory();
	int amount = getNumberOfCarsInMemory();
	if (c == NULL) {
		printf("%s\n", "printAllCarsInMemory(): the memory array has not been initialized");
		return;
	}
	
	printf("%s%d\n {", "printAllCarsInMemory():\n amount = ", amount);
	for (int i = 0; i < amount; i++) {
		//printf("{make: %s, model: %s, year: %d, price: %d, id: %d}\n", c->make, c->model, c->year, c->price, c->uniqueID);
		printf("%d, ", c->uniqueID);
		c++;
	}
	printf("}\n");
}

void printAllCarsOnDisk() {
	car *c = getAllCarsOnDisk();
	int amount = getNumberOfCarsOnDisk();
	
	printf("%s%d\n {", "printAllCarsOnDisk():\n amount = ", amount);
	for (int i = 0; i < amount; i++) {
		//printf("{make: %s, model: %s, year: %d, price: %d, id: %d}\n", c->make, c->model, c->year, c->price, c->uniqueID);
		printf("%d, ", c->uniqueID);
		c++;
	}
	printf("}\n");
}

void printMemory() {
	printf("amount of memory used: %d\n", getAmountOfUsedMemory());
	printf("getNumberOfCarsInMemory(): %d\n", getNumberOfCarsInMemory());
	printf("getNumberOfCarsOnDisk(): %d\n", getNumberOfCarsOnDisk());
}

void addManyCars(int amount) {
	printf("adding cars: %d\n", amount);
	if (amount <= 0) return;
	for(;amount > 0; amount--) {
		addCar("make", "model", 6, 8989, id++);
	}
}

int main(int argc, char const *argv[])
{
	testMaxMemoryAndAddCar();
	testGetCarById();
	testModifyCarById();
	testDeleteCarById();
	return 0;
}