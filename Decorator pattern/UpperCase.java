package filebonus;
public class UpperCase extends FilesHandler{   
       
    //Constructor
	public UpperCase(FileInterface fileInterface)   
    {      
        super(fileInterface);
    }  
    
    // UpperCase functionality
    @Override       
    public String toModify(String message)   
    {              
        String upperCase="";
        for(int i=0; i<message.length();i++)
        {
          char c = message.charAt(i);
        	int a = (int)c; 
          boolean lower = (a>=97 && a<=122);  
            if(lower)
            {                
                a = a-32;                
            }
            upperCase+=(char)a;
        }
        return  upperCase;   
    }   

}
