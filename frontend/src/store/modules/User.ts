export interface User {
    userInfo: {
        id: number | null
        username: string
        password: string
        email: string
        is_staff: boolean
        is_active: boolean
        date_joined: string
    }
    accessToken: string
    refreshToken: string
}
