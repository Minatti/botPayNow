# botPayNow
Automation Project

Minimalist design sketch (steps)


1. task_payment

    1.1: Open browser by URL
    1.2: Search fields of inputs for (cpf/cnpj and propert Code), capturing your elements
    1.3: Click on element button 'Confirmar'
    1.4: Find the element in the table and validate the contents
    1.5: Content Ok... Click ON content for open modal dialog.
    1.6: Here, let's choose the download option, this option will download the PDF file and here we finish the first step of the process, let's go to the next one!

2. read_pdf

    1.1: We'll use the Tabula library to help us get data from the PDF.
        *To install run the command: pip install tabula
        ** Successfully installed numpy-1.25.1 tabula-1.0.5
    1.2: Let's create a process to open the downloaded file and scan the information, the contents of that file.
