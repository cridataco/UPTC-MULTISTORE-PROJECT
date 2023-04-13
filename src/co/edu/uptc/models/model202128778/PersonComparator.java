package co.edu.uptc.models.model202128778;

import co.edu.uptc.pojos.Person;

import java.util.Comparator;

public class PersonComparator {
    public static Comparator<Person> comparatorByPersonName = new Comparator<Person>() {
        @Override
        public int compare(Person o1, Person o2) {
            Person p1 = (Person) o1;
            Person p2 = (Person) o2;
            return p1.getName().compareTo(p2.getName());
        }
    };

    public static Comparator<Person> comparatorByPersonCode = new Comparator<Person>() {
        @Override
        public int compare(Person o1, Person o2) {
            Person p1 = (Person) o1;
            Person p2 = (Person) o2;
            return p1.getCode().compareTo(p2.getCode());
        }
    };


    public static Comparator<Person> comparatorByPersonId = new Comparator<Person>() {
        @Override
        public int compare(Person p1, Person p2) {
            String p1Id = "" + p1.getId();
            String p2Id = "" + p2.getId();
            return p1Id.compareTo(p2Id);
        }
    };
}
