class Vehicle:
    def __init__(self, vehicle_number, seating_capacity):
        self.vehicle_number = vehicle_number
        self.seating_capacity = seating_capacity
        self.trips = []

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, new_vehicle_number):
        self.vehicle_number = new_vehicle_number

    def get_seating_capacity(self):
        return self.seating_capacity

    def set_seating_capacity(self, new_seating_capacity):
        self.seating_capacity = new_seating_capacity

    def get_trips(self):
        return self.trips

    def add_trip(self, trip):
        self.trips.append(trip)


class Trip:
    def __init__(self, vehicle, pick_up_location, drop_location, departure_time):
        self.vehicle = vehicle
        self.pick_up_location = pick_up_location
        self.drop_location = drop_location
        self.departure_time = departure_time
        self.booked_seats = 0

    def get_vehicle(self):
        return self.vehicle

    def get_pick_up_location(self):
        return self.pick_up_location

    def set_pick_up_location(self, new_pick_up_location):
        self.pick_up_location = new_pick_up_location

    def get_drop_location(self):
        return self.drop_location

    def set_drop_location(self, new_drop_location):
        self.drop_location = new_drop_location

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_booked_seats(self):
        return self.booked_seats

    def set_booked_seats(self, new_booked_seats):
        self.booked_seats = new_booked_seats


class Location:
    def __init__(self, name, service_ptr=None):
        self.name = name
        self.service_ptrs = []
        self.trips = []

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_service_ptr(self,droplocation):
        for i in self.service_ptrs:
            if i.get_depature_location()==droplocation:
                return i
        return None 

    def set_service_ptr(self, droplocation,Service_Object):
        for i in self.service_ptrs:
            if i.get_drop_location()==drop_location:
                return 
        else:
            self.service_ptrs.append(Service_Object)        

    def add_trip(self, trip):
        if trip.get_pick_up_location() != self.name:
            return
        else:
            self.trips.append(trip)
            
    def add_service_ptr(self,service):
        self.service_ptrs.append(service)
        

class BinaryTreeNode:
    def __init__(self, departure_time=0, trip_node_ptr=None, parent_ptr=None):
        self.left_ptr = None
        self.right_ptr = None
        self.parent_ptr = parent_ptr
        self.departure_time = departure_time
        self.trip_node_ptr = trip_node_ptr

    def get_left_ptr(self):
        return self.left_ptr

    def set_left_ptr(self, new_left_ptr):
        self.left_ptr = new_left_ptr

    def get_right_ptr(self):
        return self.right_ptr

    def set_right_ptr(self, new_right_ptr):
        self.right_ptr = new_right_ptr

    def get_parent_ptr(self):
        return self.parent_ptr

    def set_parent_ptr(self, new_parent_ptr):
        self.parent_ptr = new_parent_ptr

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_trip_node_ptr(self):
        return self.trip_node_ptr

    def set_trip_node_ptr(self, new_trip_node_ptr):
        self.trip_node_ptr = new_trip_node_ptr


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_height(self):

        def height(node):
            if not node:
                return 0
            else: return max(height(node.left_ptr), height(node.right_ptr))+1
       
            
        return height(self.root)

 
    def Inorder_Traversal(self,root):
        result=[]

        def recursive_traversal(current,result):

            if current is not None:
                recursive_traversal(current.left_child)
                result.append(current)
                
                recursive_traversal(current.right_child)

        recursive_traversal(root,result)
        return result 
        

    def get_number_of_nodes(self):
        # Return the number of nodes in the tree (not implemented here)
        def count(root):
            if root is None:
                return 0
            else:
                return count(root.get_left_ptr()) + count(root.get_right_ptr())+1


        return count(self.root)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def get_element_with_minimum_key(self):
        current=self.root
        while current.get_left_ptr() is not None :
            current=current.get_left_ptr()
        # Return the element with the minimum key (not implemented here)
        return current 

    def get_element_with_maximum_key(self):
        current=self.root
        while current.get_right_ptr() is not None :
            current=current.get_right_ptr()
        
        return current 

    def search_node_with_key(self, key):
        current=self.root
        while current:
                
                if (key==current.get_departure_time()):
                    
                    return current 
                elif (key<current.get_departure_time()):
                    current=current.get_left_ptr()
                    
                else:
                    current=current.get_right_ptr()   
                    
        return None            
        # Search for a node with the given key (not implemented here)
        
    def get_successor_node(self, node):
        if node is None :
            return None
        if node.get_right_ptr():
            current=node.get_right_ptr()
        else:
            return None    

        while current:
            if current.get_left_ptr() is not None:
                current=current.get_left_ptr()
            else:
                return current     



        
        

        # Find the successor node of the given node (not implemented here)
        

    def get_predecessor_node(self, node):
        if node is None :
            return None
        if node.get_left_ptr():
            current=node.get_left_ptr()
        else:
            return None     

        while current:
            if current.get_right_ptr() is not None :
                current=current.get_right_ptr()
            else:
                return current     
        

class TransportService:
    def __init__(self, location_ptr=None, bst_head=None,departure_location=None):
        self.location_ptr = location_ptr
        self.bst_head = bst_head
        self.departure_location=departure_location



    def insertnode(self,Tree_Object,root):
        if Tree_Object.get_departure_time()<=root.get_departure_time():
            if root.get_left_ptr() is None:
                root.set_left_ptr(Tree_Object)
                Tree_Object.set_parent_ptr(root)
            else:
                return self.insertnode(Tree_Object,root.get_left_ptr())
        elif Tree_Object.get_departure_time()>root.get_departure_time():
            if root.get_right_ptr() is None:
                root.set_right_ptr(Tree_Object)
                Tree_Object.set_parent_ptr(root)
            else:
                return self.insertnode(Tree_Object,root.get_right_ptr())     
    def delete_node(self,node):
        if self.bst_head==node:
            if self.bst_head.get_left_ptr() is not None:
                current=self.bst_head.get_left_ptr()
                while current.get_right_ptr() is not None:
                    current=current.get_right_ptr()       
                current.set_right_ptr(self.bst_head.get_right_ptr()) 

                temp_left=self.bst_head.get_left_ptr()
                temp_left.set_parent_ptr(None)
                temp_right=self.bst_head.get_right_ptr()
                temp_right.set_parent_ptr(current)
                self.bst_head=temp_left

            else:
                self.bst_head=self.bst_head.get_right_ptr()
                self.bst_head.set_parent_ptr(None)


        else:
            parent = node.get_parent_ptr()

            if node.get_left_ptr() is None and node.get_right_ptr() is None:
                if parent.get_left_ptr() == node:
                    parent.set_left_ptr(None)
                else:
                    parent.set_right_ptr(None)

            elif node.get_left_ptr() is None:
                if parent.get_left_ptr() == node:
                    parent.set_left_ptr(node.get_right_ptr())
                else:
                    parent.set_right_ptr(node.get_right_ptr())
                node.get_right_ptr().set_parent_ptr(parent)

            elif node.get_right_ptr() is None:
                if parent.get_left_ptr() == node:
                    parent.set_left_ptr(node.get_left_ptr())
                else:
                    parent.set_right_ptr(node.get_left_ptr())
                node.get_left_ptr().set_parent_ptr(parent)

            else:
                node = node.get_right_ptr()
                while node.get_left_ptr() is not None:
                    node = node.get_left_ptr()

                node.set_key(node.get_key())
                node.set_data(node.get_data())

                if node.get_parent_ptr().get_left_ptr() == node:
                    node.get_parent_ptr().set_left_ptr(node.get_right_ptr())
                else:
                    node.get_parent_ptr().set_right_ptr(node.get_right_ptr())

                if node.get_right_ptr():
                    node.get_right_ptr().set_parent_ptr(node.get_parent_ptr())


    def get_depature_location(self):
        return self.departure_location   
    def get_location_ptr(self):
        return self.location_ptr

    def set_location_ptr(self, new_location_ptr):
        self.location_ptr = new_location_ptr

    def get_bst_head(self):
        return self.bst_head

    def set_bst_head(self, new_bst_head):
        self.bst_head = new_bst_head

    def get_node(self,departure_time,vehicle_number):
        if (self.bst_head.get_departure_time()==departure_time) and (self.bst_head.get_trip_node_ptr().get_vehicle().get_vehicle_number()==vehicle_number):
            return self.bst_head
        else:
            current=self.bst_head  
            while current:
                if (departure_time==current.get_departure_time()) and (current.get_trip_node_ptr().get_vehicle().get_vehicle_number()==vehicle_number):
                    return current 
                elif (departure_time<current.get_departure_time()) and (current.get_trip_node_ptr().get_vehicle().get_vehicle_number()==vehicle_number):
                    current=current.get_left_ptr()
                else:
                    current=current.get_right_ptr()    
    def add_trip(self, key, trip):
        Tree_Object=BinaryTreeNode(departure_time=key,trip_node_ptr=trip)
        self.insertnode(Tree_Object,self.bst_head)
        pass
    def delete_trip(self,departure_time):
        self.delete_node(self.get_node(departure_time))



class TravelDesk:
    def __init__(self):
        self.vehicles = []
        self.locations = []

   
                

            


   
               
    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        # Check if the vehicle already exists, if not, create a new one with the seating capacity (not implemented here)
        vehicle = None
        for i in self.vehicles:
            if i.get_vehicle_number()==vehicle_number:
                vehicle=i
            
        if vehicle is None:
            vehicle=Vehicle(vehicle_number=vehicle_number,seating_capacity=seating_capacity) 
            self.vehicles.append(vehicle)
        Trip_Object=Trip(vehicle=vehicle,pick_up_location=pick_up_location,drop_location=drop_location,departure_time=departure_time)
        Location_Object=None
        for j in self.locations:
            if j.get_name()==pick_up_location:
                    Location_Object=j
        if Location_Object is None :
            Location_Object=Location(name=pick_up_location)
            self.locations.append(Location_Object)
        Location_Object.add_trip(Trip_Object)
        Service_Object=None 
        
        for i in Location_Object.service_ptrs:
            if i.get_depature_location()==drop_location:
                Service_Object=i
        if Service_Object is None:
            Tree_Object=BinaryTreeNode(departure_time=departure_time,trip_node_ptr=Trip_Object)
            Service_Object=TransportService(location_ptr=Location_Object,departure_location=drop_location)
            Service_Object.set_bst_head(Tree_Object)
            Location_Object.add_service_ptr(Service_Object)

        else:
            Service_Object.add_trip(key=departure_time,trip=Trip_Object)



        # Create a new trip and add it to the appropriate objects (not implemented here)

        # Create or retrieve the Location object and associated pick up location (not implemented here)


        # Add the trip to the TransportService's BST (not implemented here)

    def show_trips(self, pick_up_location, after_time, before_time):
        result=[]
        if after_time>before_time:
            before_time,after_time=after_time,before_time
        for i in self.locations:
            
            if i.name==pick_up_location:
                
                location=i
                for j in location.trips:
                    
                    if j.get_departure_time()<before_time and j.get_departure_time()>after_time:
                        result.append(j)
        return result        
        
    def show_tripsbydestination(self, pick_up_location, destination,after_time, before_time):
        result=[]
        if after_time>before_time:
            before_time,after_time=after_time,before_time
        for i in self.locations:
            
            if i.name==pick_up_location:
                
                location=i
                for j in location.trips:
                    
                    if j.get_departure_time()<before_time and j.get_departure_time()>after_time and j.get_drop_location()==destination:
                        result.append(j)

        # Retrieve the relevant TransportService of specific destination first then iterate over the BST to find trips within a specified time range (not implemented here)
        return result
             
        # Retrieve the relevant TransportService first then iterate over the BST to find trips within a specified time range (not implemented here)


    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
        
        for i in self.locations:
            if i.name==pick_up_location:
                Location=i 
        
        for j in Location.service_ptrs:
            if j.get_depature_location()==drop_location:
                Service_Object=j
            else:
                return None     
        
        Node=Service_Object.get_node(departure_time,vehicle_number)
       
        if Node.get_trip_node_ptr().get_booked_seats()<=Node.get_trip_node_ptr().get_vehicle().get_seating_capacity()-1:
            Node.get_trip_node_ptr().set_booked_seats(Node.get_trip_node_ptr().get_booked_seats()+1)
        else:
            print("heloo")
            Service_Object.delete_trip(departure_time)    
            return None
        # Find the corresponding trip to book the seat and have proper validation (not implemented here)
        return Node.get_trip_node_ptr()
       


   

                        


                    
                    