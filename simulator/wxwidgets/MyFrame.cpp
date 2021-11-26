#include "MyFrame.hpp"
#include <iostream>


// Constructor.
MyFrame::MyFrame() : wxFrame(nullptr, wxID_ANY, "Sample App", wxPoint(50, 50), wxSize(800, 600))
{
    auto menuBar = new wxMenuBar;

    // menu.
    auto menuFile = new wxMenu;
    menuFile->Append(wxID_OPEN, _T("&Open"));
    menuFile->Append(wxID_SAVE, _T("&Save"));
    menuFile->AppendSeparator();

    menuBar->Append(menuFile, "File");

    SetMenuBar(menuBar);

    // panel.
    panel = new wxPanel(this, wxID_ANY, wxPoint(0,0), wxSize(100,100));
    // button.
    button = new wxButton(panel, wxID_HIGHEST, _T("Hello World"), wxPoint(5,5), wxSize(100, 100));
    // text box.
    textbox = new wxTextCtrl(panel, wxID_HIGHEST, _T(""), wxPoint(10,10), wxSize(100, 20), wxTE_PROCESS_ENTER);

    // event handler.
    Bind(wxEVT_CLOSE_WINDOW, &MyFrame::onClose, this);
    Bind(wxEVT_MENU, &MyFrame::click, this);

    button->Bind(wxEVT_BUTTON, &MyFrame::onPaint, this);
    textbox->Bind(wxEVT_TEXT_ENTER, &MyFrame::onEnter, this);

    // lambda version.
    // Bind(wxEVT_MENU, [this](wxCommandEvent&) { Close(true); }, wxID_EXIT);
}

// Destructor.
MyFrame::~MyFrame()
{
}

void MyFrame::onClose(wxCloseEvent& event)
{
    std::cout << "close" << std::endl;
    Destroy();
}

void MyFrame::click(wxCommandEvent& event)
{
    int eventId = event.GetId();
    if (eventId == wxID_OPEN) {
        std::cout << "open, " << "clicked!!" << std::endl;
    } else if (eventId == wxID_SAVE) {
        std::cout << "save, " << "clicked!!" << std::endl;
    } else if (eventId == wxID_EXIT) {
        std::cout << "close" << std::endl;
        Close(true);
    }
}

void MyFrame::onPaint(wxCommandEvent& event)
{
    // delete textbox;
    std::cout << "click button!!" << "clicked!!" << std::endl;
    std::cout << textbox->GetValue() << std::endl;
}

void MyFrame::onEnter(wxCommandEvent& event)
{
    std::cout << textbox->GetValue() << std::endl;
}
