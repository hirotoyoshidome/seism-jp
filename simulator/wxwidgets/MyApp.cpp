#include "MyApp.hpp"
#include "MyFrame.hpp"


// declare.
wxDECLARE_APP(MyApp);

bool MyApp::OnInit()
{
    if(!wxApp::OnInit())
        return false;

    MyFrame* frame = new MyFrame;
    frame->Show();

    return true;
}

// implement.
wxIMPLEMENT_APP(MyApp);
