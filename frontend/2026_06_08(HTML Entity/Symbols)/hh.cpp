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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <pre>
    1. Less Than =>  &lt;
    2. Greater Than =>  &gt;
    4. Ampersand  =>  &amp;
    </pre>
    <table border>
        <tr> <td>
                Character
            </td>
            <td>
                Entity Name
           </td>
            <td>
                Entity Number
            </td>
            <td>
                Output
            </td>
        </tr>
        <tr>
        <td>Less than</td>
        <td>&amp;lt;</td>
        <td>&amp;#60;</td>
        <td>&lt;</td>
        </tr>
        <tr>
        <td>Greater Than</td>
        <td>&amp;gt;</td>
        <td>&amp;#62;</td>
        <td>&gt;</td>
        </tr>
        <tr>
            <td>Ampersand</td>
            <td>&amp;amp;</td>
            <td>&amp;#38;</td>
            <td>&amp;</td>
        </tr>
        <tr>
            <td>Double Quote</td>
            <td>&quot;</td>
        </tr>
    </table>
</body>
</html>
    
)";
// 2. Clean and format the string into a Data URL scheme
std::string cleanHtml = cleanHtmlForUrl(htmlContent);
std::string systemCommand = "open -a \"Google Chrome\" \"data:text/html," + cleanHtml + "\"";
// 3. Execute the command to tigger the default browser instantly
std::cout << "Launching browser directly from memory..." << std::endl;
std::system(systemCommand.c_str());

return 0;

}