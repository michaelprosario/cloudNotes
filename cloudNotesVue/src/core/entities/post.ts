
  export default class Post {
    title: string;
    abstract?: string; // Optional excerpt
    content: string;
    tags: string[];
    createdAt: number;
    createdBy: string;
  
    constructor() {
        this.title = '';
        this.abstract = '';
        this.content = '';
        this.tags = [];
        this.createdAt = 0;
        this.createdBy = '';
    }
  }
  