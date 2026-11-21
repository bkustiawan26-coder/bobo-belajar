from app.models.identity import GuardianChildLink, GuardianConsent, ParentProfile, StudentProfile, User, UserRole
from app.models.curriculum import Chapter, CurriculumSource, CurriculumVersion, EducationLevel, Grade, LearningObjective, Subject, Topic
from app.models.content import ContentReview, ContentVersion, Lesson, LessonBlock, MediaAsset
from app.models.questions import Question, QuestionExplanation, QuestionOption, QuestionReview, QuestionSource, QuestionVersion
from app.models.assessment import Assessment, AssessmentAnswer, AssessmentQuestion, AssessmentResult, AssessmentSession, AssessmentTemplate
from app.models.learning import ExerciseAttempt, LearningRecommendation, LearningSession, LessonProgress, MasteryRecord
from app.models.ai import AIConversation, AIMessage, AIModel, AIPromptVersion, AIProvider, AISafetyEvent, AIUsageLog, KnowledgeChunk, KnowledgeDocument
from app.models.ops import AuditLog, Notification, Payment, PrivacyRequest, Subscription, SubscriptionEntitlement, SyncJob

__all__ = [
    "User", "UserRole", "ParentProfile", "StudentProfile", "GuardianChildLink", "GuardianConsent",
    "EducationLevel", "Grade", "CurriculumVersion", "CurriculumSource", "Subject", "Chapter", "Topic", "LearningObjective",
    "Lesson", "LessonBlock", "MediaAsset", "ContentVersion", "ContentReview",
    "Question", "QuestionVersion", "QuestionOption", "QuestionExplanation", "QuestionSource", "QuestionReview",
    "AssessmentTemplate", "Assessment", "AssessmentQuestion", "AssessmentSession", "AssessmentAnswer", "AssessmentResult",
    "LearningSession", "LessonProgress", "ExerciseAttempt", "MasteryRecord", "LearningRecommendation",
    "AIProvider", "AIModel", "AIPromptVersion", "AIConversation", "AIMessage", "AIUsageLog", "AISafetyEvent", "KnowledgeDocument", "KnowledgeChunk",
    "Subscription", "SubscriptionEntitlement", "Payment", "Notification", "AuditLog", "SyncJob", "PrivacyRequest",
]
