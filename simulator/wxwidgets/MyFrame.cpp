#include "MyFrame.hpp"


MyFrame::MyFrame() : wxFrame(nullptr, wxID_ANY, "Minimal App")
{
    auto menuBar = new wxMenuBar;
    auto menuFile = new wxMenu;
    menuFile->Append(wxID_EXIT, "Quit");
    menuBar->Append(menuFile, "File");
    SetMenuBar(menuBar);

    Bind(wxEVT_CLOSE_WINDOW, &MyFrame::OnClose, this);
    Bind(wxEVT_MENU, [this](wxCommandEvent&) { Close(true); }, wxID_EXIT);
}

MyFrame::~MyFrame()
{
}

void MyFrame::OnClose(wxCloseEvent& event)
{
    Destroy();
}
