class AnalyticsWorker:
    def __init__(self):
        self.description = "The Analytics Worker is a software project designed to handle large-scale data processing and analytics tasks."
        self.features = {
            "Scalability": "The Analytics Worker is designed to handle massive data sets and scale horizontally to meet increasing demand.",
            "Fault Tolerance": "The system is built to automatically recover from failures, ensuring minimal downtime and maximum data availability.",
            "Real-Time Processing": "The project uses streaming data processing to provide real-time insights and analytics.",
            "Data Visualization": "The system includes a data visualization module to present complex data in an intuitive and user-friendly format.",
            "Security": "The Analytics Worker includes robust security features to protect sensitive data and ensure compliance with industry regulations."
        }
        self.technologies = {
            "Programming Languages": ["Java", "Python"],
            "Frameworks": ["Spring Boot", "Flask"],
            "Databases": ["Apache Cassandra", "MongoDB"],
            "Message Queue": ["Apache Kafka"],
            "Data Visualization": ["D3.js", "Chart.js"],
            "Operating System": ["Linux (Ubuntu)"]
        }
        self.prerequisites = {
            "Java": "8 or later",
            "Python": "3.6 or later",
            "Apache Cassandra": "3.11 or later",
            "MongoDB": "3.6 or later",
            "Apache Kafka": "2.7 or later"
        }
        self.installation_steps = [
            "Clone the repository: `git clone https://github.com/your-username/analytics-worker.git`",
            "Install dependencies: `mvn install` (for Java dependencies) and `pip install -r requirements.txt` (for Python dependencies)",
            "Configure the system: Update configuration files (e.g., `application.properties`, `database.properties`) to match your environment",
            "Start the system: `mvn spring-boot:run` (for Java) or `python app.py` (for Python)",
            "Verify the system: Use a tool like `curl` or a web browser to test the API endpoints"
        ]

    def get_description(self):
        return self.description

    def get_features(self):
        return self.features

    def get_technologies(self):
        return self.technologies

    def get_prerequisites(self):
        return self.prerequisites

    def get_installation_steps(self):
        return self.installation_steps

# Example usage:
if __name__ == "__main__":
    analytics_worker = AnalyticsWorker()
    print(analytics_worker.get_description())
    for feature, description in analytics_worker.get_features().items():
        print(f"{feature}: {description}")
    for technology, values in analytics_worker.get_technologies().items():
        print(f"{technology}: {', '.join(values)}")
    for prerequisite, version in analytics_worker.get_prerequisites().items():
        print(f"{prerequisite}: {version}")
    for step in analytics_worker.get_installation_steps():
        print(step)