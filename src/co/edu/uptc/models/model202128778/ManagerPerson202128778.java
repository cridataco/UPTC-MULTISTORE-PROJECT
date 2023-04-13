package co.edu.uptc.models.model202128778;

import co.edu.uptc.pojos.Person;

import java.util.ArrayList;
import java.util.List;

public class ManagerPerson202128778 {
    List<Person> listPeople;
    private Manager202128778 managerGeneral;

    public ManagerPerson202128778(Manager202128778 managerGeneral) {
        this.managerGeneral = managerGeneral;
        listPeople = new ArrayList<>();
    }

    public void addPerson(Person person){
        if (person.getName().equals("") || person.getCode().equals("")) {
            managerGeneral.presenter.notifyError("Información incompleta");
        } else {
            listPeople.add(person);
            managerGeneral.presenter.notifyPeopleUpdated();
        }
    }

    public Person getPerson(String attribute){
        for (Person per: listPeople) {
            if(attribute.equals(per.getCode()) || attribute.equals(per.getName())){
                return per;
            }
        }
        return null;
    }

    public void editPerson(Person person){
        for (Person per: listPeople) {
            if(per.getId()==person.getId()){
                per.setCode(person.getCode());
                per.setName(person.getName());
                return;
            }
        }
    }

    public List<Person> getPeople() {
        List<Person> auxList = new ArrayList<>();
        for (Person person: listPeople) {
            auxList.add(person.clone());
        }
        return auxList;
    }
}
