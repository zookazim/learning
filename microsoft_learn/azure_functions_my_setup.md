[Microsoft Azure Home](microsoft_learn_home.md)

# My Setup

## Requirements

1. An Azure Account (I'm using Visual Studio subscription)
2. Install Azure Functions Core Tools (done, link below)
3. Install Python (done)
4. "Python" Extension for Visual Studio Code (done)
5. "Azure Functions" extension for Visual Studio Code (done)
6. "Azure Resources" VS Code extension


## Create Azure Function using Python V2 Model

### Create function from template in VS

#### Using Azure extension

Use shift+ctrl+p to open the command pallet and type in Azure then select Azure Function Create.


### Run Function

* Create virtual environment if not already created
```bash
python3 -m venv my_env
```


* Start virtual environment in terminal (I'm using PowerShell prompt)

```bash
> my_env/Scripts/Activate
```

```bash
(.venv) PS C:\Users\zooka\git_repos\learning\python_azure_function> func host start
Found Python version 3.10.11 (py).

Azure Functions Core Tools
Core Tools Version:       4.0.5198 Commit hash: N/A  (64-bit)
Function Runtime Version: 4.21.1.20667

[2023-06-01T08:15:16.865Z] File 'C:\Program Files\dotnet\dotnet.exe' is not found, 'dotnet' invocation will rely on the PATH environment variable.
[2023-06-01T08:15:20.332Z] File 'C:\Program Files\dotnet\dotnet.exe' is not found, 'dotnet' invocation will rely on the PATH environment variable.
[2023-06-01T08:15:21.091Z] Worker process started and initialized.

Functions:

        RoSqlGenerator:  http://localhost:7071/api/RoSqlGenerator
```

* Run function using localhost link above and "Thunder Client" which I installed on VS Code or use Postman if you have it installed.






## Links

[Install Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools)


[Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)


[Quick Start Doc](https://learn.microsoft.com/en-GB/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration)


[Quick Start example using commandline](https://github.com/yokawasa/azure-functions-python-samples/blob/master/docs/quickstart-v2-python-functions.md)

[Create CI/CD Pipeline for Azure Devops](https://medium.com/globant/how-to-create-and-deploy-a-python-azure-function-using-azure-devops-ci-cd-2aa8f8675716)

[Nice tutorial for Azure Functions in Python](https://towardsdatascience.com/tutorial-of-python-azure-functions-81949b1fd6db)

