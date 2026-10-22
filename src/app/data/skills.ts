export interface Skill {
  name: string;
  icon?: string; // clase de Devicon; si no tiene, se muestra solo el nombre
}

export interface SkillGroup {
  title: string;
  skills: Skill[];
}

// Verificá los nombres de los íconos en https://devicon.dev
export const SKILL_GROUPS: SkillGroup[] = [
  {
    title: 'Lenguajes',
    skills: [
      { name: 'Python', icon: 'devicon-python-plain' },
      { name: 'TypeScript', icon: 'devicon-typescript-plain' },
      { name: 'JavaScript', icon: 'devicon-javascript-plain' },
      { name: 'C#', icon: 'devicon-csharp-plain' },
      { name: 'SQL' },
      { name: 'HTML', icon: 'devicon-html5-plain' },
      { name: 'CSS', icon: 'devicon-css3-plain' },
    ],
  },
  {
    title: 'Frameworks y librerías',
    skills: [
      { name: 'Django', icon: 'devicon-django-plain' },
      { name: 'Django REST Framework' },
      { name: 'Flask', icon: 'devicon-flask-original' },
      { name: 'Celery' },
      { name: 'Angular', icon: 'devicon-angular-plain' },
      { name: 'Bootstrap', icon: 'devicon-bootstrap-plain' },
      { name: 'Tailwind CSS', icon: 'devicon-tailwindcss-original' },
      { name: 'Unity', icon: 'devicon-unity-plain' },
    ],
  },
  {
    title: 'Bases de datos',
    skills: [
      { name: 'MySQL', icon: 'devicon-mysql-original' },
      { name: 'MariaDB', icon: 'devicon-mariadb-original' },
      { name: 'MongoDB', icon: 'devicon-mongodb-plain' },
      { name: 'Redis', icon: 'devicon-redis-plain' },
    ],
  },
  {
    title: 'DevOps y nube',
    skills: [
      { name: 'Docker', icon: 'devicon-docker-plain' },
      { name: 'Git', icon: 'devicon-git-plain' },
      { name: 'GitHub', icon: 'devicon-github-original' },
      { name: 'GitLab', icon: 'devicon-gitlab-plain' },
      { name: 'Linux', icon: 'devicon-linux-plain' },
      { name: 'AWS (fundamentos)', icon: 'devicon-amazonwebservices-plain-wordmark' },
    ],
  },
  {
    title: 'Datos e IA',
    skills: [
      { name: 'Pandas', icon: 'devicon-pandas-plain' },
      { name: 'Tableau' },
      { name: 'scikit-learn', icon: 'devicon-scikitlearn-plain' },
      { name: 'TensorFlow', icon: 'devicon-tensorflow-original' },
      { name: 'NLTK' },
    ],
  },
  {
    title: 'E-learning y Realidad Extendida',
    skills: [
      { name: 'Moodle (integraciones)', icon: 'bi bi-mortarboard' },
      { name: 'Paquetes SCORM', icon: 'bi bi-box-seam' },
      { name: 'Desarrollo para Meta Quest', icon: 'bi bi-headset-vr' },
      { name: 'Telemetría de simulaciones', icon: 'bi bi-graph-up' },
    ],
  },
];