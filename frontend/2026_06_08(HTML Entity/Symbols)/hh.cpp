#include <iostream>
#include <string>
#include <cstdlib>

// helper function to remove newlines and extra spaces for the URL strinf
std::string cleanHtmlForUrl(std::string html){
    std::string cleanText = " ";
    for (char c : html){
        // ONLY skip line break. Let macOS handle spaces and quotes natively!
        if (c == '\n' || c == '\r'){
            continue;
        }
        cleanText += c;
    }
    return cleanText;
}
int main(){
    // 1. Define your HTML structure using a raw string literal
    std::string htmlContent = R"(

    
)";
// 2. Clean and format the string into a Data URL scheme
std::string cleanHtml = cleanHtmlForUrl(htmlContent);
std::string systemCommand = "open -a \"Google Chrome\" \"data:text/html," + cleanHtml + "\"";
// 3. Execute the command to tigger the default browser instantly
std::cout << "Launching browser directly from memory..." << std::endl;
std::system(systemCommand.c_str());

return 0;

}