
package co.edu.uptc.models.model202113049;


import co.edu.uptc.pojos.Person;
import co.edu.uptc.presenter.ContratBills;

import java.util.List;

public class ManagerModel_202113049 implements ContratBills.Model {

    public ContratBills.Presenter presenter;

    private ManagerPerson_202113049 managerPerson;

    public ManagerModel_202113049(){
        managerPerson = new ManagerPerson_202113049(this);
    }

    @Override
    public void setPresenter(ContratBills.Presenter presenter) {
        this.presenter = presenter;
    }

    @Override
    public void addPerson(Person person) {
        managerPerson.addPerson(person.clone());
    }

    @Override
    public String getPerson(int pos) {
        return null;
    }

    @Override
    public List<Person> getPeople() {
        List<Person> auxList = managerPerson.getPeople();
        return auxList;
    }

    @Override
    public Person getPerson(String attribute) {
        return managerPerson.getPerson(attribute);
    }

    @Override
    public void editPerson(Person person) {
        managerPerson.editPerson(person);
    }

    @Override
    public String getAuthor() {
        return "DEYVID FERNANDO CRUZ MOLANO";
    }
}

