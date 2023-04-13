package co.edu.uptc.models.model202113049;

public class Node_202113049<T>{
    T info;
    private Node_202113049 less = null;
    private Node_202113049 MajorOrEqual = null;

    public Node_202113049(T info, Node_202113049 less, Node_202113049 majorOrEqual) {
        this.info = info;
        this.less = less;
        MajorOrEqual = majorOrEqual;
    }

    public Node_202113049(){
    }

    public Node_202113049(T info){
        this.info=info;
    }

    public T getInfo() {
        return info;
    }

    public void setInfo(T info) {
        this.info = info;
    }

    public Node_202113049 getLess() {
        return less;
    }

    public void setLess(Node_202113049 less) {
        this.less = less;
    }

    public Node_202113049 getMajorOrEqual() {
        return MajorOrEqual;
    }

    public void setMajorOrEqual(Node_202113049 majorOrEqual) {
        MajorOrEqual = majorOrEqual;
    }
}
