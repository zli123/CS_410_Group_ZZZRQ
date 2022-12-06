#citation
#https://learn.microsoft.com/en-us/python/api/azure-ai-textanalytics/azure.ai.textanalytics.aio.textanalyticsclient?view=azure-python


import os

def sample_classify_document_single_label() -> None:
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    endpoint = os.environ["https://cs410-final.cognitiveservices.azure.com/"]
    key = os.environ["5ec32f7458604485894c545cab0bd750"]
    project_name = os.environ["CS410-Final"]
    #custom trained model "new" for review classification
    deployment_name = os.environ["new"]
    
    text_analytics_client = TextAnalyticsClient(
                endpoint=endpoint,
                credential=AzureKeyCredential(key),
            )

    # open all the reviews in the the current dir for classification: postive, negative, neutral
    for filename in os.listdir(os.getcwd()):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
           
            with open(f) as fd:
                document = [fd.read()]

            poller = text_analytics_client.begin_single_label_classify(
                document,
                project_name=project_name,
                deployment_name=deployment_name
            )

            document_results = poller.result()
            for doc, classification_result in zip(document, document_results):
                if classification_result.kind == "CustomDocumentClassification":
                    classification = classification_result.classifications[0]
                    print("The document text '{}' was classified as '{}' with confidence score {}.".format(
                        doc, classification.category, classification.confidence_score)
                    )
                elif classification_result.is_error is True:
                    print("Document text '{}' has an error with code '{}' and message '{}'".format(
                        doc, classification_result.code, classification_result.message
                    ))


if __name__ == "__main__":
    sample_classify_document_single_label()