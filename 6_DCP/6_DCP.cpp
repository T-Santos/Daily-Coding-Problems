#include <iostream>
#include <stdint.h>

/* 
	XOR Doubly Linked list
	
	TODO: Need to Document
	TODO: Need to write unit tests
	TOOD: Need to organize better in XorList.h/.cpp
*/

using namespace std;

// Should it be a class with pnx being private?
struct XorNode
{
	
	string data = "";     // info for node
	XorNode *pnx = NULL;     // XOR address of Prev/Next Node address (maybe should be private
	
};

class XorList
{
	
	private:
		XorNode *head, *tail;
	
	public:
		
		XorList()
		{
			head = NULL;
			tail = NULL;
		}
		
		void print_list()
		{
			XorNode *cur_node = this->head;
			XorNode *prev_node = NULL;
			XorNode *temp_node = NULL;
			
			while(cur_node)
			{
				cout << cur_node->data << endl;
				temp_node = cur_node;
				
				// calculate the addr of the "next" node
				cur_node = (XorNode *)((uintptr_t)cur_node->pnx ^ (uintptr_t)prev_node);
				prev_node = temp_node;
			}
		}
		
		void add(XorNode* new_node)
		{
			if(!this->head)
			{
				this->head = new_node;
				this->tail = new_node;
			}else
			{
				// make a pointer to the old tail's node
				XorNode *old_tail = this->tail;
				
				// point the tail to the new node's address 
				this->tail = new_node; 
				
				// now that we have a new node, update the tail's pointer to include it's addr
				old_tail->pnx = (XorNode *)((uintptr_t)old_tail->pnx ^ (uintptr_t)new_node);
				
				// update the new tail to contain the old tail's address (aka prev XOR 0)
				new_node->pnx = old_tail;
			}
		}
		
		XorNode* get(int index)
		{
			int cur_index = 0;
			XorNode *cur_node = this->head;
			XorNode *prev_node = NULL;
			XorNode *temp_node = NULL;
			
			while(cur_node && cur_index != index)
			{
				temp_node = cur_node;
				cur_node = (XorNode *)((uintptr_t)cur_node->pnx ^ (uintptr_t)prev_node);
				prev_node = temp_node;
				cur_index++;
			}
		
			if (cur_node)
			{
				return cur_node;
			}
			else
			{
				return NULL;
			}
		}
};


int main(int argc, char** argv) {
	
	XorList my_list = XorList();
	XorNode new_node_1 = XorNode();
	XorNode new_node_2 = XorNode();
	XorNode new_node_3 = XorNode();
	
	new_node_1.data = "Kevin";
	new_node_2.data = "Tyler";
	new_node_3.data = "Santos";
	
	my_list.add(&new_node_1);
	my_list.add(&new_node_2);
	my_list.add(&new_node_3);
	
	my_list.print_list();
	
	XorNode *found_node = my_list.get(0);
	
	if (found_node)
		cout << found_node->data << endl;
	else
		cout << "Not found" << endl;
	
	return 0;
}