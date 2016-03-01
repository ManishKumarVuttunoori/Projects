package filebonus;
import java.io.*; 

public class FileImplementation implements FileInterface{   
          
    private String content;
    public FileImplementation(){this.content = null;}   
    
    @Override   
    public String getFileContents(String fileString)   
    {      
        if(fileString== null || fileString ==""){
        	System.out.println("Please enter a valid file path");
        	System.exit(0);
        }
    	this.content = "";
		FileInputStream f = null;

		try {
				f = new FileInputStream(fileString);
				int content_int;
				while ((content_int = f.read()) != -1) {
					this.content+= (char)content_int;
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} 
		catch (IOException e) {
			e.printStackTrace();
		}finally {
			try {
				if (f != null)
					f.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
        return this.content;   
    }
    public void display(){
    	if(content == null)
    		System.out.println("Please use getFileContents('file path') to read from the file before displaying it....");
    	else
    	System.out.println(content);
    }
  
}