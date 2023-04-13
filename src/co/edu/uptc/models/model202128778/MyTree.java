package co.edu.uptc.models.model202128778;

import co.edu.uptc.models.model202128778.pojos.Node;

public class MyTree {
    Node header;
    PersonComparator comparator;


    public void showTree() {
        showTreeInOrder(header);
    }

    public void showTreePreOrder(Node node) {
        System.out.println(node.getInfo());
        if (node.getLess() != null) {
            showTreePreOrder(node.getLess());
        }
        if (node.getMajor() != null) {
            showTreePreOrder(node.getMajor());
        }
    }

    public void showTreeInOrder(Node node) {
        if (node != null) {
            if (node.getLess() != null) {
                showTreeInOrder(node.getLess());
            }
            System.out.println(node.getInfo());
            if (node.getMajor() != null) {
                showTreeInOrder(node.getMajor());
            }
        } else {
            System.out.println("No hay árbol.");
        }
    }

    public void showTreePostOrder(Node node) {
        if (node.getLess() != null) {
            showTreePostOrder(node.getLess());
        }
        if (node.getMajor() != null) {
            showTreePostOrder(node.getMajor());
        }
        System.out.println(node.getInfo());
    }
}
