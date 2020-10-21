import java.io.*;
import java.nio.*;
import java.util.Scanner;

public class Converter
{
	public static void main(String[] args) 
	{
		try {
			//After you have downloaded the CSV of the excel chart to the same directory as converter
			//make sure that when you download the excel file that you call it CSV.csv
			File file = new File("CSV.csv");
			//will write to a new file that will be created (in same directory) 
			//	when you run program called UCSV
			//Every time you run program will erase previous content of UCSV
			//	I have no idea why I decided to name the new file UCSV. rename to whatever you want.
			File newFile = new File("UCSV.txt");
			newFile.createNewFile();
			Scanner s = new Scanner(file);

			FileWriter clearer = new FileWriter(newFile, false);clearer.write("");clearer.close();
			
			FileWriter fr = new FileWriter(newFile, true);

			//This will write a column of excel to a js array. 
			//Insert name of array here
			fr.write("var month6 = [");
			boolean begin = false;
			while (s.hasNextLine()) {
				//this line ensures that you don't have a comma before first value in array
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				//the columns are numbered starting from 0
				fr.write(tokens[0]);
			}
			fr.write("];\n\n");
			
			//need to create new scanner so it starts scanning from beginning of file
			//this is basically just a copy and paste for if you want to turn more than one 
			//	column into arrays
			s = new Scanner(file);
			fr.write("var numCalls6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[1]);
			}
			fr.write("];\n\n");
			/*
			//JUST DUPLICATION

			s = new Scanner(file);
			fr.write("var RT6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[2]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var assessments6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[4]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var RTassessments6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[5]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var SA6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[6]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var SO6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[7]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var gamb6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[8]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var newAdmits6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[10]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var RTNewAdmits6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[11]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var menAd6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[12]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var womanAd6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[13]);
			}
			fr.write("];\n\n");
			
			s = new Scanner(file);
			fr.write("var nonAd6 = [");
			begin = false;
			while (s.hasNextLine()) {
				if (begin) fr.write(", "); else begin = true;
				String line = s.nextLine();
				String[] tokens = line.split(",");
				fr.write(tokens[14]);
			}
			fr.write("];");
			*/
			
			fr.close();
		} catch(IOException e) {
			System.err.println("Caught IOE: " + e.getMessage());
		}
	}
}