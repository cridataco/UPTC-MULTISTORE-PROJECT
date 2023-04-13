package co.edu.uptc.models.model202128778.pojos;

public class Node<T> {
    private T info;
    private Node less;
    private Node major;

    public Node() {
    }

    public Node(T info) {
        this.info = info;
        this.less = null;
        this.major = null;
    }

    public Node(T info, Node less, Node major) {
        this.info = info;
        this.less = less;
        this.major = major;
    }

    public T getInfo() {
        return info;
    }

    public void setInfo(T info) {
        this.info = info;
    }

    public Node getLess() {
        return less;
    }

    public void setLess(Node less) {
        this.less = less;
    }

    public Node getMajor() {
        return major;
    }

    public void setMajor(Node major) {
        this.major = major;
    }

}
