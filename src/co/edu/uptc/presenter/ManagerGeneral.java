package co.edu.uptc.presenter;

import co.edu.uptc.models.model202128687.ManagerModel202128687;
import co.edu.uptc.models.model202114641.ManagerModel202114641;
import co.edu.uptc.models.model202127343.ManagerModel202127343;
import co.edu.uptc.models.model202022012.ManagerModel202022012;
import co.edu.uptc.models.model202127717.ManagerModel202127717;
import co.edu.uptc.models.model202128778.Manager202128778;
import co.edu.uptc.models.model202127812.ManagerModel202127812;
import co.edu.uptc.models.model202127061.ManagerModel202127061;
import co.edu.uptc.models.modelGerman.ManagerModel;

import co.edu.uptc.models.model202113049.ManagerModel_202113049;


import co.edu.uptc.models.model202115100.ManegerModel202115100;

import co.edu.uptc.views.board.DashBoard;


public class ManagerGeneral {
    private static ManagerGeneral instance;
    ContratBills.View view;
    ContratBills.Model modelGerman;
    ContratBills.Model model202127061;
    ContratBills.Model model202113059;
    ContratBills.Model model202128687;
    ContratBills.Model model202128778;
    ContratBills.Model  model202127343;
    ContratBills.Model model202022012;
    ContratBills.Presenter presenter;
    ContratBills.Model model202127812;
    ContratBills.Model modelSebastian;
    ContratBills.Model model202115100;
    ContratBills.Model model202127717;

    private ManagerGeneral() {
    }

    private void createMVP(){
         view = new DashBoard();
         presenter = new Presenter();
         view.setPresenter(presenter);
         presenter.setView(view);
         createModels();
         configModelUserGerman();
         configModelUserSantiago_202115100();
     }

     public static ManagerGeneral getInstance(){
         return instance==null?instance = new ManagerGeneral():instance;
     }


     private void createModels(){
         // TODO aqui se cream todos los modelos
         modelGerman = new ManagerModel();
         model202128687 = new ManagerModel202128687();
         model202128778 = new Manager202128778();
         model202113059 = new ManagerModel_202113049();
         model202127343 = new ManagerModel202127343();
         model202022012 = new ManagerModel202022012();
         model202127812 = new ManagerModel202127812();
         model202127061 = new ManagerModel202127061();
         modelSebastian= new ManagerModel202114641();
         model202115100 = new ManegerModel202115100();
         model202127717 = new ManagerModel202127717();
     }

     public void configModelUserGerman(){
         modelGerman.setPresenter(presenter);
         presenter.setModel(modelGerman);
         view.updatedPeople();
     }

    public void configModel202113049(){
        model202113059.setPresenter(presenter);
        presenter.setModel(model202113059);
        view.updatedPeople();
    }

    public void configModel202127717(){
        model202127717.setPresenter(presenter);
        presenter.setModel(model202127717);
        view.updatedPeople();
    }


    public void configModelUser202114641(){
        modelSebastian.setPresenter(presenter);
        presenter.setModel(modelSebastian);
        view.updatedPeople();
    }



    public void configModelUser202127343(){
        model202127343.setPresenter(presenter);
        presenter.setModel(model202127343);
        view.updatedPeople();
    }

    public void configModelOtherAlex() {
        presenter.setModel(model202128687);
        view.updatedPeople();
    }
    public void configModelUser202127061(){
        model202127061.setPresenter(presenter);
        presenter.setModel(model202127061);
        view.updatedPeople();
    }
    public void configModelUserSantiago_202115100(){
        model202115100.setPresenter(presenter);
        presenter.setModel(model202115100);
        view.updatedPeople();
    }

    public void configModel202127812(){
        model202127812.setPresenter(presenter);
        presenter.setModel(model202127812);
        view.updatedPeople();
    }


    public void configBryanModel(){
        // TODO  aqui se configura para cado estudiante el modelo y este metodo se llama desde la vista
        model202022012.setPresenter(presenter);
        presenter.setModel(model202022012);
        view.updatedPeople();
    }

    public void configModel202128778(){
        model202128778.setPresenter(presenter);
        presenter.setModel(model202128778);
        view.updatedPeople();
    }

    public void runProject(){
        createMVP();
        view.start();
    }

}
