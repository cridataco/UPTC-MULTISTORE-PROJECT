package co.edu.uptc.models.model202127717;

import co.edu.uptc.pojos.Person;

public class Node {
    private Person info;
    private Node minor=null;
    private Node greaterEqual =null;

    public Node(Person info) {
        this.info = info;
    }

    public Person getInfo() {
        return info;
    }

    public Node getMinor() {
        return minor;
    }

    public void setMinor(Node minor) {
        this.minor = minor;
    }

    public Node getGreaterEqual() {
        return greaterEqual;
    }

    public void setGreaterEqual(Node greaterEqual) {
        this.greaterEqual = greaterEqual;
    }
}
