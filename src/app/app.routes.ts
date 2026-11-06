import { ResolveFn, Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { ProjectDetail } from './pages/project-detail/project-detail';
import { PROFILE } from './data/profile';
import { inject } from '@angular/core';
import { ProjectService } from './core/project-service';

const SITE_TITLE = `${PROFILE.name} | ${PROFILE.role}`;

// Título de cada caso de estudio, según el slug de la URL
const projectTitle: ResolveFn<string> = route => {
  const project = inject(ProjectService).getBySlug(route.paramMap.get('slug') ?? '');
  return project ? `${project.title} | ${PROFILE.name}` : SITE_TITLE;
};

export const routes: Routes = [
    {
        path: '',
        component: Home,
        title: SITE_TITLE
    },
    { 
        path: 'proyectos/:slug', 
        component: ProjectDetail,
        title: projectTitle
    },
    { 
        path: '**', 
        redirectTo: '' 
    },
];
