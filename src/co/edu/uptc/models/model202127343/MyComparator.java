package co.edu.uptc.models.model202127343;

import co.edu.uptc.pojos.Person;

public class MyComparator {

    public MyComparator(){

    }

    public int personComparetor(Person p1, Person p2){
        if(p1.getId() == p2.getId()){
            return 0;
        }
        if(p1.getId() > p2.getId()){
            return 1;
        } else {
            return -1;
        }
    }
}
