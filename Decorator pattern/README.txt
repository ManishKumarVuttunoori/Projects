Name: Manish Kumar Vuttunoori
Email: manivutt@indiana.edu
Bonus Assignment  P565 SE

Submission includes the following files in the filebonus package:
    1. FileInterface.java
    2. FileImplementation.java
    3. FilesHandler.java
    4. Encrypt.java
    5. UpperCase.java
    6. README.txt
    
    
STEPS for adding a new behavior to the existing functionalities:

Please see, I am taking the example of adding lowerCase functionality to the existing module without making any modifications to the 
previously existing code.

	1. Create a class that extends the FilesHandler as follows
		Example:
		public class LowerCase extends FilesHandler{}
		
	2. Create a constructor that takes an object of any class that implements FileInterface as follows:
		Example:
		public LowerCase(FileInterface fileInterface)   
    	{      
        	super(fileInterface);
    	}  
	3. Override the abstract method i.e toModify() method which takes a string as input to add the new behavior as follows.
		Example:
		public String toModify(String content){
		
		    // add your code here.....
		}
		
		
STEPS for using the features in Main Class.
    1. In your main method, Create an object for FileImplementation. This object is must to perform remaining operations such as encryption,
     converting to upperCase or LowerCase etc.
    
        Examples:
        //  FileInterface implementer   = new FileImplementation(); 
		//	FileInterface implementer = new Encrypt(new FileImplementation());
			FileInterface implementer = new UpperCase(new FileImplementation());                      ...... I am using this statement for my example
		//  FileInterFace implementer = new LowerCase(new FileImplementation());
		//FileInterface implementer = new UpperCase(new Encrypt(new FileImplementation()));
	
	2. Use the getFileContents() method to read contents from a file. 
	Note: getFileContents method takes the file path as input. and returns the contents based on the 
	functionality that was invoked.	
		
		Example:
		String output = implementer.getFileContents("C:\\Users\\Public\\Desktop\\resume.txt");
		
		Here, output contains the file contents converted to upperCase letters.  
	
	3.  The output can be used for other purposes or can also display it. Alternately, user can also use the display method, which is available with all the objects that 
	implement FileInterface 	
		NOTE: Before using the display method, you have to call the getFileContents method so as to read the file contents. Else you would receive a message asking you 
		to call the method getFileContents(filePath).
		
		Example:
		implementer.display();	
		
		