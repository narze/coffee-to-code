class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Linklist:
	def __init__(self):
		self.head=None		
	def add(self,new_data):
		new_node=Node(new_data)
		if(self.head!=None):
			current_node=self.head
			while(current_node.next!=None):
				current_node=current_node.next
			current_node.next=new_node
		else:
			self.head=new_node		
	def printAll(self):
		current_node=self.head
		while(current_node!=None):
			print(current_node.data,end='')
			current_node=current_node.next
	def replace(self,data):
		check=False
		current_node=self.head
		while(current_node!=None):
			if current_node.data==data:
				current_node.data='d'
			current_node=current_node.next
	def frequency_count(self):
		a=[]
		current_node=self.head
		while(current_node!=None):
			if current_node.data not in a:
				a.append(current_node.data)
			else:
				self.delete(current_node.data)											
			current_node=current_node.next					
	def delete(self,data):
		current_node=self.head
		while current_node.next!=None:
			if current_node.next.data==data:
				break
			current_node=current_node.next	
		current_node.next=current_node.next.next																	
	def run(self,text):
		link =Linklist()
		for i in text:
			link.add(i)
		link.replace('f')
		link.frequency_count()	
		link.printAll()
if __name__ == "__main__":		
	a=Linklist()
	a.run('coffee')	




























    
