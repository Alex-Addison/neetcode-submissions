//iostream is std input library, vector is for data
#include <iostream>
#include <vector>

//this is the class for a node
class Node {
//public class used for variables 
//we can access from outside this class
public:
    //data is the value
    int data;
    //* represents a pointer to a node object
    //pointer is stored in the variable next
    Node* next;

    //constructor for when just data is given
    //initialize data to data and next to nullptr
    Node(int data) : data(data), next(nullptr) {

    }

    //constructor overload to use next if given
    Node(int data, Node* next) : data(data), next(next) {

    }
};

class LinkedList {
//privately declare head as a Node*
private:
    Node* head;
public:
    //initialize head to null
    LinkedList() : head(nullptr) {
        
    }

    // 1. Get value at index (0-based)
    int get(int index) {
        //create temp ptr to head
        Node* curr = head;
        //while curr is not nullptr and idx>0
        while (curr && index > 0) {
            //curr is the value of curr's next
            //dereferences pointer, then grabs .next
            curr = curr->next;
            index--;
        }
        //if curr is null, return -1
        if (!curr) return -1;
        //dereference curr, then return curr.data
        return curr->data;
    }

    // 2. Insert at head
    void insertHead(int val) {
        Node* node = new Node(val);
        node->next = head;
        head = node;
    }

    // 3. Insert at tail
    void insertTail(int val) {
        Node* node = new Node(val);
        if (!head) {
            head = node;
            return;
        }
        Node* curr = head;
        while (curr->next) {
            curr = curr->next;
        }
        curr->next = node;
    }

    // 4. Remove node at index (returns true if removed)
    bool remove(int index) {
        if (!head) return false;
        if (index == 0) {
            Node* tmp = head;
            head = head->next;
            delete tmp;
            return true;
        }
        Node* curr = head;
        for (int i = 0; curr->next && i < index - 1; ++i)
            curr = curr->next;
        if (!curr->next) return false;
        Node* tmp = curr->next;
        curr->next = curr->next->next;
        delete tmp;
        return true;
    }

    // 5. Get all values as a vector
    std::vector<int> getValues() {
        std::vector<int> vals;
        Node* curr = head;
        while (curr) {
            vals.push_back(curr->data);
            curr = curr->next;
        }
        return vals;
    }
};
