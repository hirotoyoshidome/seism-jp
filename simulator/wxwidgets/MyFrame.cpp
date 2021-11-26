#include "MyFrame.hpp"
#include <iostream>


// Constructor.
MyFrame::MyFrame() : wxFrame(nullptr, wxID_ANY, "Sample App")
{
    auto menuBar = new wxMenuBar;

    // sample menu.
    auto menuFile = new wxMenu;
    menuFile->Append(wxID_OPEN, _T("&Open"));
    menuFile->Append(wxID_SAVE, _T("&Save"));
    menuFile->AppendSeparator();

    menuBar->Append(menuFile, "File");

    SetMenuBar(menuBar);

    // event handler.
    Bind(wxEVT_CLOSE_WINDOW, &MyFrame::OnClose, this);
    Bind(wxEVT_MENU, &MyFrame::click, this);

    // lambda version.
    // Bind(wxEVT_MENU, [this](wxCommandEvent&) { Close(true); }, wxID_EXIT);
}

// Destructor.
MyFrame::~MyFrame()
{
}

void MyFrame::OnClose(wxCloseEvent& event)
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
