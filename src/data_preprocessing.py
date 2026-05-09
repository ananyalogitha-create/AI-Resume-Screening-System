import pandas as pd
import numpy as np
import re
from typing import List, Dict

class DataPreprocessor:
    """Simple resume data preprocessing"""
    
    def __init__(self):
        self.resume_data = None
    
    def load_resumes(self, csv_file: str) -> pd.DataFrame:
        """Load resumes from CSV file"""
        self.resume_data = pd.read_csv(csv_file)
        return self.resume_data
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Convert to lowercase
        text = text.lower()
        # Remove special characters
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def preprocess_resumes(self, df: pd.DataFrame) -> pd.DataFrame:
        """Preprocess all resumes in dataframe"""
        df_clean = df.copy()
        if 'resume_text' in df_clean.columns:
            df_clean['resume_text'] = df_clean['resume_text'].apply(self.clean_text)
        return df_clean
    
    def load_job_description(self, job_file: str) -> str:
        """Load job description from text file"""
        with open(job_file, 'r', encoding='utf-8') as f:
            job_desc = f.read()
        return self.clean_text(job_desc)
    
    def get_statistics(self, df: pd.DataFrame) -> Dict:
        """Get basic statistics about resumes"""
        stats = {
            'total_resumes': len(df),
            'missing_values': df.isnull().sum().to_dict(),
            'columns': df.columns.tolist()
        }
        return stats
