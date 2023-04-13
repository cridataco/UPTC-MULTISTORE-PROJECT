package co.edu.uptc.models.model202127343;

public class Node<G> {

    private G info;
    private Node<G> less = null;
    private Node<G> majorAndEqual = null;

    public Node(G info, Node<G> less, Node<G> majorAndEqual) {
        this.info = info;
        this.less = less;
        this.majorAndEqual = majorAndEqual;
    }

    public Node(G info){
        this.info = info;
    }

    public Node(){

    }

    public G getInfo() {
        return info;
    }

    public void setInfo(G info) {
        this.info = info;
    }

    public Node<G> getLess() {
        return less;
    }

    public void setLess(Node<G> less) {
        this.less = less;
    }

    public Node<G> getMajorAndEqual() {
        return majorAndEqual;
    }

    public void setMajorAndEqual(Node<G> majorAndEqual) {
        this.majorAndEqual = majorAndEqual;
    }
}
