package co.edu.uptc.views.board;

import co.edu.uptc.utils.UtilComponents;
import co.edu.uptc.utils.UtilImages;
import co.edu.uptc.views.Globals.ColorPalette;
import co.edu.uptc.views.Globals.ValuesGlobals;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;

public class PanelMenu extends JPanel {



    class ItemMenu {
        String text;
        int level;
        boolean isSelectable;

        public ItemMenu(String text, int level,boolean isSelectable) {
            this.text = text;
            this.level = level;
            this.isSelectable = isSelectable;
        }
    }
    ArrayList<ItemMenu> listItemMenu ;
    private JLabel imageLabel ;
    UtilComponents utilComponents;

    private DashBoard dashBoard;

    public PanelMenu(DashBoard dashBoard) {
        this.dashBoard = dashBoard;
      configGlobal();
        loadMenu();
      initializeComponents();
    }

    private void loadMenu(){
        listItemMenu = new ArrayList<>();
        listItemMenu.add( new ItemMenu("MENÚ",0,false));
        listItemMenu.add( new ItemMenu("Personas",1,true));
        listItemMenu.add( new ItemMenu("Mapa",1,true));
        listItemMenu.add( new ItemMenu("Salir",1,true));

    }


    private void configGlobal(){
        setBackground(ValuesGlobals.COLOR_BACK_PANEL_MENU);
        setPreferredSize(new Dimension(250,0));
        setSize(new Dimension(250,0));
        this.setBorder(ValuesGlobals.BORDER_PANEL);
        setLayout(null);
        utilComponents = new UtilComponents();

    }



    private void initializeComponents() {
        addImage();
        utilComponents.setAuxY((int)imageLabel.getLocation().getY()+imageLabel.getHeight());
        for (ItemMenu val: listItemMenu) {
            //addItemMenu(val.text,30,val.level,val.isSelectable);
            addItemMenu(val,30);
        }
    }

    private PanelMenu getInstance(){
        return this;
    }



    private void addImage(){
        UtilImages utilImages = new UtilImages();
        imageLabel = new JLabel();
        imageLabel.setBounds(10,10,this.getWidth()-20,this.getWidth()-60);
        Icon img = utilImages.loadScaleImage(ValuesGlobals.PATH_IMAGE_MENU,imageLabel.getWidth(),imageLabel.getHeight());
        imageLabel.setIcon(img);
        add(imageLabel);
    }



    private void addItemMenu(ItemMenu itemMenu,int x){
        JLabel jLabel = new JLabel(itemMenu.text);
      //  jLabel.setOpaque(true);
        jLabel.setBackground(ValuesGlobals.COLOR_BACK_PANEL_MENU);
        jLabel.setFont(ValuesGlobals.FONT_MENU_UNSELECT);

        if (itemMenu.level>0)
            x = x+30;
        jLabel.setBounds(x,0,150,30);

        JLabel finalJLabel = (JLabel) utilComponents.locateComponentY(jLabel);
        add(finalJLabel);

        jLabel.addMouseListener(new MouseListener() {
            @Override
            public void mouseClicked(MouseEvent e) {
            }
            @Override
            public void mousePressed(MouseEvent e) {
               showPanel(itemMenu);

            }
            @Override
            public void mouseReleased(MouseEvent e) {
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                if (itemMenu.isSelectable) {
                    finalJLabel.setFont(ValuesGlobals.FONT_MENU_SELECT);
                }
            }

            @Override
            public void mouseExited(MouseEvent e) {
                finalJLabel.setFont(ValuesGlobals.FONT_MENU_UNSELECT);
            }
        });
    }




    private void showPanel(ItemMenu itemMenu){
        switch (itemMenu.text){
            case "Personas": {
                dashBoard.showPanelPeople();
                break;
            }
            case "Mapa": {
              dashBoard.showPanelMap();
                break;
            }
            case "Salir": {
                validateClose();
                break;
            }
        }
    }

    private void validateClose(){
        int input =JOptionPane.showConfirmDialog(this.dashBoard, "Esta seguro de salir?",
                "YES_NO_CANCEL_OPTION", JOptionPane.YES_NO_OPTION,
                JOptionPane.INFORMATION_MESSAGE);
        if (input == 0) {
            System.exit(0);
        }


    }


}
