package distributed_systems_homework_ASM;

import java.io.IOException;
import java.io.File;

public class Main
{
	public static void main(String[] args) {
		try {
			Server s = new Server(new File(args[0]));
			Client c = new Client();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}