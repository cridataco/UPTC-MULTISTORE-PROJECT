package co.edu.uptc.models.modelGerman;

import co.edu.uptc.models.modelGerman.ManagerPerson;
import co.edu.uptc.pojos.Person;
import co.edu.uptc.presenter.ContratBills;

import java.util.List;

public class ManagerModel implements ContratBills.Model {
    public ContratBills.Presenter presenter;

    private ManagerPerson managerPerson;

    public ManagerModel(){
        managerPerson = new ManagerPerson(this);
    }


    public void setPresenter(ContratBills.Presenter presenter) {
        this.presenter = presenter;
    }


    public void addPerson(Person person) {
        managerPerson.addPerson(person.clone());
    }

    public String getPerson(int pos) {
        return null;
    }


    public List<Person> getPeople() {
        List<Person> auxList = managerPerson.getPeople();
        return auxList;
    }


    public Person getPerson(String attribute) {
        return managerPerson.getPerson(attribute);
    }


    public void editPerson(Person person) {
        managerPerson.editPerson(person);
    }


    public String getAuthor() {
        return "German Amezquita Becerra";
    }
}
