#ifndef MYFRAME_H
#define MYFRAME_H

#include <wx/wx.h>


class MyFrame : public wxFrame
{
public:
    // Constructor.
    MyFrame();

    // Destructor.
    virtual ~MyFrame();

    void OnClose(wxCloseEvent& event);
    void click(wxCommandEvent& event);
};

#endif
