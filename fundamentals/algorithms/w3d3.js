// nodes and singly linked lists

class ListNode {
    constructor(value) {
        this.next = null;
        this.value = value;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    addToHead(value) {
        let new_node = new ListNode(value);

        if (this.head == null && this.tail == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            new_node.next = this.head;
            this.head = new_node;
        }
    }

    

    addToTail(value) {
        let new_node = new ListNode(value);

        if (this.head == null && this.tail == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            this.tail.next = new_node;
            this.tail = new_node;
    }
}

    display() {

        let output = "";

        let runner = this.head;

        while (runner != null) {
            output += runner.value;
            if (runner.next != null) {
                output += " - ";
            }
            runner = runner.next;
        }

        console.log(output);
    }


    contains(value) {
        // returns true if the linked list contains a node with the given value
        // false otherwise
            let runner = this.head;
    
            while (runner != null) {
                if (runner.value == value) {
                    return true;
                }

                runner = runner.next;
            }
            return false;
        }
}

var new_sll = new SinglyLinkedList();

new_sll.addToHead(8);
new_sll.addToHead(3);
new_sll.addToHead(6);





new_sll.display(); // 6 - 3 - 8

new_sll.addToTail(4);

new_sll.display(); // 6 - 3 - 8 - 4

new_sll.addToTail(7); // 6 - 3 - 8 - 4 - 7

console.log(new_sll.contains(4)) // true
console.log(new_sll.contains(6)) // true
console.log(new_sll.contains(7)) // true
console.log(new_sll.contains(11)) // false



