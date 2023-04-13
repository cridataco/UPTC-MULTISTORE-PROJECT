package co.edu.uptc.models.model202127812;

import co.edu.uptc.pojos.Person;

public class Node {
    private Person info;
    private Node minor=null;
    private Node mayorEqual=null;

    public Node(Person info) {
        this.info = info;
    }

    public Node(Person info, Node minor, Node mayorEqual) {
        this.info = info;
        this.minor = minor;
        this.mayorEqual = mayorEqual;
    }

    public Person getInfo() {
        return info;
    }

    public void setInfo(Person info) {
        this.info = info;
    }

    public Node getMinor() {
        return minor;
    }

    public void setMinor(Node minor) {
        this.minor = minor;
    }

    public Node getMayorEqual() {
        return mayorEqual;
    }

    public void setMayorEqual(Node mayorEqual) {
        this.mayorEqual = mayorEqual;
    }
}
