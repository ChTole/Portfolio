// import { Service } from '@angular/core';

// @Service()
// export class ProjectService {}
import { Injectable } from '@angular/core';
import { PROJECTS } from '../data/projects';
import { Project } from '../data/project.model';

@Injectable({ providedIn: 'root' })
export class ProjectService {
  getAll(): Project[] {
    return PROJECTS;
  }

  getBySlug(slug: string): Project | undefined {
    return PROJECTS.find(p => p.slug === slug);
  }
}