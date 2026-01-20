# System Architecture Diagram

```mermaid
flowchart LR

    subgraph DataLayer["Data Layer"]
        RawData["Raw Data Sources"]
        Features["Feature Pipeline"]
    end

    subgraph Platform["ML Platform Layer"]
        Train["Training Pipeline"]
        Registry["Model Registry"]
        Serve["Serving Pipeline"]
        Monitor["Monitoring Pipeline"]
        Retrain["Retraining Pipeline"]
    end

    subgraph UseCases["Use Case Layer"]
        LP["Late Payment"]
        FR["Invoice Fraud"]
        CR["Churn Risk"]
    end

    subgraph AppLayer["Application Layer"]
        API["Azure Functions APIs"]
        UI["Web UI"]
        Batch["Batch Interface"]
    end

    RawData --> Features
    Features --> Train
    Train --> Registry
    Registry --> Serve
    Serve --> API
    API --> UI
    API --> Batch

    Serve --> Monitor
    Monitor --> Retrain
    Retrain --> Train

    UseCases --> Train
    UseCases --> Serve