#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include<fstream>
#include <string>
#include <openssl/hmac.h>
            //include custom header files...
#include "../include/Client.h"
#include "../include/FileObject.h"
using namespace std;

Client::Client(nc_args_t clnt_arg)
{

	     //intitialize the destination Address..		
	    //Zero out structure
	memset(&destinationAddress, 0, sizeof(destinationAddress));		
	verboseMode=clnt_arg.verbose;
    memset(&destinationAddress, 0, sizeof(destinationAddress)); // Zero out structure
	destinationAddress = clnt_arg.destaddr;		
	offSet = 0;  numBytes = 0;      
	int count = 0;       //  initialising memory variables.....
	    // SOCKET creation.....
 	sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

	if (sock < 0)
	{
		HelperClass::TerminateApplication("Socket Creation Failed!!");
	}

	if(verboseMode)
	{
		cout<<"Socket Creation Successfull!!"<<endl;
	}
	
	    // connecting socket to the server    
	if (connect(sock, (struct sockaddr *) &destinationAddress, sizeof(destinationAddress)) < 0)
	{      
		HelperClass::TerminateApplication("connect() failed");
	}
	    
	if(verboseMode)
	{
		cout<<"Connection established successfully"<<endl;
	}


    
	    // sending a string of message if in message mode.
	if(clnt_arg.message_mode)            
	{

		sendString(clnt_arg.message, HelperClass::GetDigest(clnt_arg.message),"");
	}	
	else	
	{
	      
    	FileObject clnt_File(clnt_arg.filename, clnt_arg.offset, clnt_arg.n_bytes);   // initialising file object
    	offSet = clnt_File.GetoffSet();	    
    	numBytes = clnt_File.GetNumBytes();  
        string filedata;
	    ifstream file (clnt_arg.filename,ios::in|ios::ate);	  
	  	            	
	    if(file.is_open())
	    {	  
	     file.seekg(0, ios::end);   
	  	 offMaxsize =file.tellg();cout<<file.tellg();	cout<<"offmaxsize is"<<"\n"<<offMaxsize<<endl;
	   	 file.seekg(0, ios::beg);
            // finding file size		
            if(offSet == 0)
            {
	        	
	        lsize =offMaxsize;		
            file.seekg(0, ios::beg);
	      }
	        else if((offSet >0)&&((offSet-offMaxsize)<0))
	        {
		        file.seekg(offSet, ios::end); 
		        lsize = file.tellg();  
		        file.seekg(offSet, ios::beg);
         	  }
		else
		{
			HelperClass::TerminateApplication("offSet is negative or out of bounds");
		}
		
            //numBytes is less than zero, we will send, every byte from offset till EOF.        
            if(numBytes >= 0)
            {    
	             if(numBytes <= lsize)		     
	             {
                     	lsize = numBytes;                      
	             }
	             else
	             {                       
                	 	HelperClass::TerminateApplication("numBytes exceeding limit or is negative");
	             }
            }
	    else
	    {                       
        	     HelperClass::TerminateApplication("numBytes is negative");
	    }		    		  								     								
		cout<<"Printing file size"<<lsize<<"\n";
        char* memblock = new char [lsize+1];
        file.read (memblock, lsize);
		memblock[lsize]='\0';
				
            
	    if (memblock == NULL) 
	    {
	        fputs ("Memory error",stderr); 
        	exit (2);
	    }
            filedata.append(memblock,lsize);
           	cout<<"length of string s is "<<filedata.length()<<"\n";               
         	file.close();        
           	cout << "the entire file content is in memory"<<endl;

        	delete[] memblock;

    }      
        else
        {
            HelperClass::TerminateApplication("Unable to open file");
        }
        cout<<"before sending"<<endl;
        string S(clnt_arg.filename);
	    int Tag=S.find_last_of("/");
	
       	string NoSlash=S.substr(Tag+1);    // removing the slashes and giving only the file name as input...

        sendString(filedata, HelperClass::GetDigest(filedata), NoSlash);	       // sending loaded buffer with file name into the string...
        close(sock);	
	}
}

void Client::sendString(string message,const char * digest, string fileName="")
{   
    try
    {
          
            string d(digest);       
            string MSG="";     
            if(fileName!="")
            {            
                MSG.append(STARTPACKETTAG);
                MSG.append(STARTFILENAMETAG);
                MSG.append(fileName);            
                MSG.append(ENDFILENAMETAG);
                MSG.append(STARTBODYTAG);
                MSG.append(message);
                MSG.append(ENDBODYTAG);
                MSG.append(STARTDIGESTTAG);
                MSG.append(d);
                MSG.append(ENDDIGESTTAG);
                MSG.append(ENDPACKETTAG);
            }
            else
            {
                MSG = STARTPACKETTAG+STARTBODYTAG+message+ENDBODYTAG+STARTDIGESTTAG+d+ENDDIGESTTAG+ENDPACKETTAG;  
            }
            if(verboseMode)
            {
                //cout<<"Packet to be sent is:\n"<<MSG<<endl;
            }    
            size_t messageLen = MSG.length(); // determining the length of the string....
            cout<<"Length of the packet is "<<MSG.length();
            ssize_t msgDesc = send(sock, MSG.data(), messageLen, 0);

            if(msgDesc < 1)
            {
                HelperClass::TerminateApplication("send() failed");
            }
            else if(msgDesc != messageLen)
            {
                HelperClass::TerminateApplication("send() failed due to incorrect no. of bytes");
            }
	
	        if(verboseMode)
	        {
	            cout<<"message sent successfully"<<endl;
	        }	
    }
    
    catch(...)
    {
                HelperClass::TerminateApplication("sending failed");
    }          
                
} 
