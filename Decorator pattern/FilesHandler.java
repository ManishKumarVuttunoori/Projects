package filebonus;
public  abstract class FilesHandler implements FileInterface{

    public FileInterface fileInterface;
    public String content;
    public FilesHandler( FileInterface fileInterface)
    {
        this.fileInterface = fileInterface;
        content = null;
    }    
    public String getFileContents(String fileName)   {            
        content = toModify(fileInterface.getFileContents(fileName));      
        return content;   
    }         
    public void display(){
    	if(content == null)
    		System.out.println("Please use getFileContents('file path') to read from the file before displaying it....");
    	else
    	System.out.println(content);
    }
    // function that has to be overridden to add new behavior or functionality
    abstract public String toModify(String content);
}