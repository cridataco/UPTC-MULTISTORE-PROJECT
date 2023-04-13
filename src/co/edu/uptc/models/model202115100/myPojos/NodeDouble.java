package co.edu.uptc.models.model202115100.myPojos;

public class NodeDouble<T> {
    private T data;
    private NodeDouble<T> previous;
    private NodeDouble<T> next;

    public NodeDouble() {
        data = null;
        previous = null;
        next = null;
    }

    public NodeDouble(T data) {
        this.data = data;
        previous = null;
        next = null;
    }

    public NodeDouble(T data, NodeDouble<T> previous, NodeDouble<T> next) {
        this.data = data;
        this.previous = previous;
        this.next = next;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public NodeDouble<T> getPrevious() {
        return previous;
    }

    public void setPrevious(NodeDouble<T> previous) {
        this.previous = previous;
    }

    public NodeDouble<T> getNext() {
        return next;
    }

    public void setNext(NodeDouble<T> next) {
        this.next = next;
    }
}