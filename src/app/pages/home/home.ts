import { Component, inject } from '@angular/core';
import { ProjectService } from '../../core/project-service';
import { ProjectCard } from '../../shared/project-card/project-card';
import { PROFILE } from '../../data/profile';
import { SKILL_GROUPS } from '../../data/skills';
import { RouterLink } from '@angular/router';
import { SocialLinks } from '../../shared/social-links/social-links';

@Component({
  imports: [
    RouterLink, ProjectCard, SocialLinks
  ],
  selector: 'app-home',
  styleUrl: './home.css',
  templateUrl: './home.html',
})
export class Home {
  protected readonly profile = PROFILE;
  protected readonly projects = inject(ProjectService).getAll();
  protected readonly skillGroups = SKILL_GROUPS;
}
