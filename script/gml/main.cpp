#include "SampleSaxHandler.hpp"

#include <iostream>

#include <xercesc/sax2/SAX2XMLReader.hpp>
#include <xercesc/sax2/XMLReaderFactory.hpp>
#include <xercesc/util/PlatformUtils.hpp>

using namespace std;
using namespace xercesc;


int main()
{
    cout << "start." << endl;

    // TODO
    // read local gml.
    // std::ifstream ifs("./53392546_bldg_6697_op2.gml");
    // std::string contents;
    // if (ifs.fail()) {
    //     std::cerr << "Failed to open file." << std::endl;
    //     return -1;
    // }
    // while (getline(ifs, contents)) {
    //     cout << contents << endl;
    // }


    try {
        XMLPlatformUtils::Initialize();
        cout << "init." << endl;
    }
    catch (const XMLException& toCatch) {
        cerr << "init error." << endl;
        return 1;
    }

    SAX2XMLReader* parser = XMLReaderFactory::createXMLReader();
    cout << "parser init." << endl;

    try {
        SampleSaxHandler handler;
        cout << "hander init." << endl;
        parser->setContentHandler(&handler);
        cout << "parse start." << endl;
        parser->parse("./example.xml");
        cout << "parse end." << endl;
    } catch (...) {
        cerr << "load error." << endl;
    }

    delete parser;

    XMLPlatformUtils::Terminate();

    cout << "end." << endl;
    return 0;
}
