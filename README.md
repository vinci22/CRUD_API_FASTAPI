# CRUD-api-users
 a api for users CRUD, this api are conecte to a service of mysql that service is found local
 thus te conecction is make localy
 
 # info 
 this api run in a viertualenv 
 
 # NOTE:
   ## the endpoint are the next
   ### localhost/users
        this endpoint define the method read of the CRUD
        
   ### localhost/create
      this endpoint define the method create of the CRUD
      and pase the ip of the host wich realize the petition 
    
   ### localhost/delete
      
      this endpoint define the method delete of the CRUD
      in this case the "delete" are not fisic delete,rather 
      is a update method which send a flag for the state of 
      the user (delete or active)  
