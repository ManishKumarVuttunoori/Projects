package filebonus;

public class Encrypt extends FilesHandler{   
           
    // Constructor
    public Encrypt(FileInterface fileInterface)   
    {      
        super(fileInterface); 
        
    }      
    
    // encrypt functionality
    public String toModify(String message)   
    {      
        String encrypted="";
        for(int i=0; i< message.length();i++)
        {
        	char c = message.charAt(i);
        	int a = (int)c;
          boolean upper = (a>=65 && a<= 90); 
          boolean lower = (a>=97 && a<=122);  
	        if( upper || lower)
	        {
	            if(upper)
	            {
	                if(a+2>90)
	                {    
	                	a = 65+ (a+2)%90;    
	                }
	                else{ 
	                	a = a+2;                        
	                }
	            }
	            else
	            {
	                if(a+2>122)
	                {    a = 97+ (a+2)%122;
	   
	                }
	                else{ 
	                	a = a+2;
	                }
	            }
	        }
	        encrypted+= (char)a;
	    }
        return  encrypted;   
    }   

}
