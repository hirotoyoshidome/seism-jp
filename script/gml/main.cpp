#include <iostream>
#include <fstream>
#include <string>
#include <memory>
#include <vector>
#include <locale>

#include <xercesc/util/PlatformUtils.hpp>
#include <xercesc/sax/HandlerBase.hpp>
#include <xercesc/sax/AttributeList.hpp>
#include <xercesc/parsers/SAXParser.hpp>
#include <xercesc/framework/MemBufInputSource.hpp>

using namespace std;
using namespace xercesc;

#define XERCES_STATIC_LIBRARY 


class ParseHandler : public HandlerBase
{
public:
    virtual void characters(const XMLCh* const chars, const XMLSize_t length) {}
    virtual void endDocument() {}
    virtual void endElement(const XMLCh* const name) {}
    virtual void ignorableWhitespace(const XMLCh* const chars, const XMLSize_t length) {}
    virtual void processingInstruction(const XMLCh* const target, const XMLCh* const data) {}
    virtual void resetDocument() {}
    virtual void startDocument() {}
    void startElement(const XMLCh* const name, xercesc::AttributeList& attributes)
    {
        // string element(name);
        // if ( element == "a" ) {
        //     string value(attributes.getValue("href"));
        //     if ( !value.empty() ) urls.push_back(value);
        // }
    }

    vector<string> urls;
};




int main(int argc, char* argv[])
{
    cout << "start." << endl;

    // read local gml.
    std::ifstream ifs("./53392546_bldg_6697_op2.gml");
    std::string contents;

    if (ifs.fail()) {
        std::cerr << "Failed to open file." << std::endl;
        return -1;
    }

    // TODO
    // while (getline(ifs, contents)) {
    //     cout << contents << endl;
    // }

    try {
        XMLPlatformUtils::Initialize();
    }
    catch (const XMLException& toCatch) {
        cout << "init error." << endl;
        return 1;
    }

    // TODO sample.
    {
        string xhtml = "<?xml version='1.0' ?><html><body><a href=\"http://qiita.com/episteme\">επιστημη</a><img src=\"https://pbs.twimg.com/profile_images/54608127/epi_normal.jpg\"/></body></html>";
    
        auto parser = make_unique<SAXParser>();
        auto handler = make_unique<ParseHandler>();

        MemBufInputSource source(reinterpret_cast<const XMLByte*>(xhtml.data()), xhtml.size()*sizeof(wchar_t), "xhtml-parse", false);
        parser->setDocumentHandler(handler.get());
        parser->parse(source);

        // wcout.imbue(locale("japanese"));
        for ( const string& url : handler->urls ) {
            cout << url << endl;
        }
    }



    XMLPlatformUtils::Terminate();

    cout << "end." << endl;
    return 0;
}
