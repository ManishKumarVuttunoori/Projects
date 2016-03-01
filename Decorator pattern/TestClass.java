package filebonus;

public class TestClass {

	public static void main(String[] args) {
		/**** 
		 *   This is a test class to help in understanding the program flow.
		 * 	Uncomment each of the below lines one at a time to test the functionality.
		 * provide the absolute path as input to the following function.   Below I have provided a sample string for absolute path
		 * ***/
		FileInterface implementer = new FileImplementation();
		FileInterface implementer1 = new Encrypt(implementer);
			FileInterface implementer2 = new UpperCase(implementer1);
			FileInterface implementer4 = new UpperCase(implementer);
			FileInterface implementer3   = new Encrypt(implementer4); 
		
		implementer.getFileContents("C:\\Users\\Public\\Desktop\\resume.txt");
		implementer1.getFileContents("C:\\Users\\Public\\Desktop\\resume.txt");
		implementer2.getFileContents("C:\\Users\\Public\\Desktop\\resume.txt");
		implementer3.getFileContents("C:\\Users\\Public\\Desktop\\resume.txt");
		implementer4.getFileContents("C:\\Users\\Public\\Desktop\\resume.txt");
		
		// display the contents.		
		implementer.display();
		implementer1.display();
		implementer2.display();
		implementer3.display();
		implementer4.display();
	}

}
