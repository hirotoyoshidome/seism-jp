#include <wx/wx.h>


// sample
// https://qiita.com/mod_poppo/items/8e6baa50765e8573f883


class MyApp : public wxApp
{
    virtual bool OnInit() override;
};

wxDECLARE_APP(MyApp);

class MyFrame : public wxFrame
{
public:
    MyFrame();
    virtual ~MyFrame();

    void OnClose(wxCloseEvent& event);
};

bool MyApp::OnInit()
{
    if(!wxApp::OnInit())
        return false;

    MyFrame* frame = new MyFrame;
    frame->Show();

    return true;
}

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

wxIMPLEMENT_APP(MyApp);
