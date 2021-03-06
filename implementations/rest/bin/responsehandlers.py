#add your custom response handler class to this module

#the default handler , does nothing , just passes the raw output directly to STDOUT
class DefaultResponseHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type):        
        print_xml_stream(raw_response_output)
          
        
        
class MyResponseHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type):        
        print_xml_stream("foobar")

    

#HELPER FUNCTIONS
    
# prints XML stream
def print_xml_stream(s):
    print "<stream><event><data>%s</data></event></stream>" % encodeXMLText(s)

def encodeXMLText(text):
    text = text.replace("&", "&amp;")
    text = text.replace("\"", "&quot;")
    text = text.replace("'", "&apos;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text
